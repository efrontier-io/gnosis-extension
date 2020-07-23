# -*- coding: utf-8 -*-

# API to work with Gnosis Protocol order
#
# Efficient Frontier, 2020
from ccxt.base.errors import InvalidOrder, OrderNotFound, InsufficientFunds
from dataclasses import dataclass, asdict
from functools import partial
from eth_typing import Hash32
import os
from datetime import datetime
import time
import json
import logging
import requests
from typing import Dict, List, Iterable, Optional
from web3 import Web3, Account

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from . gnosis.graphql_schema import graphql_schema as schema  # generated
from . gnosis.errors import TokenNotFoundException, UnknownTokenException, GasTooHigh

__version__ = '2.0.0'

GAS_GNOSIS_ORDER = 144_000
GAS_GNOSIS_BATCH_ORDER = 98_000  # per order
GAS_GNOSIS_CANCEL_ORDER = 40_000  # per order

class TokenPair:
    base = None  # type: CryptoToken
    quote = None  # type: CryptoToken
    symbol = None

    def __getitem__(self, token):
        if self.base.symbol == token:
            return self.base
        elif self.quote.symbol == token:
            return self.quote
        else:
            raise KeyError(f"Token {token} not found")

    def __init__(self, symbol, tokens_dict):
        base, quote = symbol.split('/')
        self.symbol = symbol
        self.base = tokens_dict[base]
        self.quote = tokens_dict[quote]

    def __str__(self):
        return self.symbol


@dataclass
class CryptoToken:
    id: str
    address: str
    name: str
    symbol: str
    decimals: int

    def __post_init__(self):
        self.decimals = int(self.decimals)

    def from_raw_amount(self, int_amount: int) -> float:
        return float(int_amount / 10 ** self.decimals)

    def to_raw_amount(self, amount) -> int:
        return int(amount * (10 ** self.decimals))

    @classmethod
    def from_schema(cls, token):
        return CryptoToken(id=token.id, address=token.address, name=token.name, symbol=token.symbol,
                           decimals=int(token.decimals))


@dataclass
class Trade:
    """
    # {
    #   'id': id,                   # The trade ID.
    #   'timestamp': timestamp,     # The timestamp in milliseconds when trade has happened (batch's TS???)
    #   'datetime': date,           # UTC Datetime object (kept for backwards compatibility)
    #   'price': price,             # Trade price.
    #   'amount': amount,           # Trade volume.
    #   'side': side,               # Either 'buy' or 'sell'
    #   'symbol': ,                 # Pair symbol (ie: 'ETH/BTC'). From order.
    #   'takerOrMaker': 'maker'     # Not relevant in dfusion, use default  'maker'
    #   'info': t,                  # The JSON returned from the exchange. Stored as a dictionary, not a string.
    # }

    """
    id: str
    timestamp: int
    datetime: datetime
    price: float
    amount: int
    side: str
    symbol: str
    takerOrMaker: str
    info: Dict

    @classmethod
    def from_schema(cls, token_pair, trade: schema.Trade):
        params = {}

        if trade.order.sell_token.symbol == token_pair.base.symbol and \
                trade.order.buy_token.symbol == token_pair.quote.symbol:
            params['side'] = 'sell'
            params['amount'] = token_pair.base.from_raw_amount(int(trade.sell_volume))
            if int(trade.sell_volume) == 0:
                params['price'] = 0
            else:
                params['price'] = token_pair.quote.from_raw_amount(
                    int(trade.buy_volume)) / token_pair.base.from_raw_amount(int(trade.sell_volume))

        elif trade.order.buy_token.symbol == token_pair.base.symbol and \
                trade.order.sell_token.symbol == token_pair.quote.symbol:
            params['side'] = 'buy'
            if int(trade.buy_volume) == 0:
                params['amount'] = 0
                params['price'] = 0
            else:
                params['amount'] = token_pair.base.from_raw_amount(int(trade.buy_volume))
                params['price'] = token_pair.quote.from_raw_amount(
                    int(trade.sell_volume)) / token_pair.base.from_raw_amount(int(trade.buy_volume))

        else:
            raise InvalidOrder(
                f"Trade token pair is different. Buy {trade.order.buy_token.symbol} Sell {trade.order.sell_token.symbol}")
            # raise UnknownTokenException((trade.order.sell_token.symbol, trade.order.buy_token.symbol))

        params['symbol'] = str(token_pair)
        params['takerOrMaker'] = 'maker'
        params['id'] = trade.id
        params['timestamp'] = int(trade.trade_epoch) * 1000
        params['datetime'] = datetime.utcfromtimestamp(int(trade.trade_epoch)).isoformat()
        params['info'] = dict(
            sell_volume=int(trade.sell_volume),
            buy_volume=int(trade.buy_volume),
            trade_batch_id=int(trade.trade_batch_id),
            create_epoch=int(trade.create_epoch),
            buy_symbol=trade.order.buy_token.symbol,
            sell_symbol=trade.order.sell_token.symbol,
            order_id=int(trade.order.order_id),
            order_owner_id=trade.order.owner.id,
            owner_id=trade.owner.id,
        )
        return Trade(**params)


@dataclass
class Order:
    """

    """
    id: int  # order id
    price: float
    amount: int
    filled: int
    remaining: int
    side: str
    symbol: str
    info: str
    timestamp: int

    @classmethod
    def from_schema(cls, token_pair, order: schema.Order):
        params = dict()
        params['info'] = dict(
            id=order.id,
            owner=order.owner.id,
            price_numerator=order.price_numerator,
            price_denominator=order.price_denominator,
            max_sell_amount=order.max_sell_amount,
            from_epoch=int(order.from_epoch),
            from_batch_id=int(order.from_batch_id),
            until_batch_id=int(order.until_batch_id),
            until_epoch=int(order.until_epoch),
            cancel_epoch=order.cancel_epoch,
            create_epoch=order.create_epoch,
            delete_epoch=order.delete_epoch,
            sold_volume=int(order.sold_volume),
            bought_volume=int(order.bought_volume),
            sell_token=order.sell_token.symbol,
            buy_token=order.buy_token.symbol,
            balance_used=0,  # we use it to help calculate fetch_balance.used
            tx_hash=order.tx_hash

        )

        if order.sell_token.symbol == token_pair.base.symbol and \
                order.buy_token.symbol == token_pair.quote.symbol:
            params['side'] = 'sell'
            params['amount'] = token_pair.base.from_raw_amount(int(order.max_sell_amount))
            params['price'] = token_pair.quote.from_raw_amount(
                int(order.price_numerator)) / token_pair.base.from_raw_amount(int(order.price_denominator))
            params['filled'] = token_pair.base.from_raw_amount(int(order.sold_volume))

            params['info']['balance_used'] = token_pair.base.from_raw_amount(
                int(order.max_sell_amount) - int(order.sold_volume))
        elif order.buy_token.symbol == token_pair.base.symbol and \
                order.sell_token.symbol == token_pair.quote.symbol:
            params['side'] = 'buy'
            price_numerator = int(order.price_numerator)

            if price_numerator > 0:
                params['price'] = token_pair.quote.from_raw_amount(
                    int(order.price_denominator)) / token_pair.base.from_raw_amount(price_numerator)
                params['amount'] = token_pair.quote.from_raw_amount(int(order.max_sell_amount) / params['price'])
            else:
                params['price'] = 0
                params['amount'] = 0
            # 1st version
            # params['filled'] = token_pair.base.from_raw_amount(int(order.bought_volume))
            # 2nd version
            params['filled'] = token_pair.quote.from_raw_amount(int(order.sold_volume) / params['price'])
            params['info']['balance_used'] = token_pair.quote.from_raw_amount(
                int(order.max_sell_amount) - int(order.sold_volume))

        else:
            raise InvalidOrder(
                f"Order token pair is different. Buy {order.buy_token.symbol} Sell {order.sell_token.symbol}")

        try:  # Some orders have incorrect values
            params['info']['datetime'] = datetime.utcfromtimestamp(int(order.from_epoch)).isoformat()
        except ValueError as ex:
            params['info']['datetime'] = None

        return Order(
            id=int(order.order_id),
            symbol=str(token_pair),
            timestamp=int(order.from_epoch) * 1000,
            remaining=params['amount'] - params['filled'],
            **params)


class GnosisExchange:
    """
    The extensions API is based on the API of the ccxt library.

    Note: All symbols have the format ETH/BTC
    All tokens should be ERC20 tokens.

    When starting to trade first time you have to approve tokens in your gnosis wallet
    https://dex.gnosis.io/wallet

    """

    #
    # When trading a new pair:
    # Add it to PAIRS
    # Hard code its tokens definitive addresses here as "anyone can add token with the same name :("

    PAIRS = ('WETH/USDT', 'WETH/USDC',)


    BATCH_SIZE = 300  # seconds
    PRODUCTION = True
    THEGRAPH_TIMEOUT = 0.1  # wait after creating an order - until the order becomes available at thegraph

    _NETWORK_CONFIGS = {
        "mainnet": {
            "allowed_tokens": {
                "USDT": "0xdac17f958d2ee523a2206206994597c13d831ec7",
                "WETH": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                "USDC": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                "DAI": "0x6b175474e89094c44da98b954eedeac495271d0f"
            },
            "token_proxies": {
                "USDC": "0x0882477e7895bdC5cea7cB1552ed914aB157Fe56"
            },
            "https_url": "https://mainnet.infura.io/v3/834b8b491c9d4e97b5c3c2e96a453ba0",
            "wss_url": "wss://mainnet.infura.io/ws/v3/834b8b491c9d4e97b5c3c2e96a453ba0",
            "contract_address": "0x6F400810b62df8E13fded51bE75fF5393eaa841F",
            "thegraph_url": "https://api.thegraph.com/subgraphs/name/gnosis/protocol",
            "etherscan_url": "https://api.etherscan.io/api",
            "gnosis_price_estimator_url": "https://dex-price-estimator.gnosis.io/api/v1/",
            "gnosis_gas_station_url": 'https://safe-relay.gnosis.io/api/v1/gas-station/',
        },
        "rinkeby": {
            "allowed_tokens": {
                "USDT": "0xa9881e6459ca05d7d7c95374463928369cd7a90c",
                "WETH": "0xc778417e063141139fce010982780140aa0cd5ab",
                "USDC": "0x4dbcdf9b62e891a7cec5a2568c3f4faf9e8abe2b",
                "DAI": "0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea"
            },
            "https_url": "https://rinkeby.infura.io/v3/834b8b491c9d4e97b5c3c2e96a453ba0",
            "wss_url": "wss://rinkeby.infura.io/ws/v3/834b8b491c9d4e97b5c3c2e96a453ba0",
            "contract_address": "0xC576eA7bd102F7E476368a5E98FA455d1Ea34dE2",
            "thegraph_url": "https://api.thegraph.com/subgraphs/name/gnosis/protocol-rinkeby",
            "etherscan_url": "https://api-rinkeby.etherscan.io/api",
            "gnosis_price_estimator_url": "https://dex-price-estimator.rinkeby.gnosis.io/api/v1/",
            "gnosis_gas_station_url": 'https://safe-relay.rinkeby.gnosis.io/api/v1/gas-station/',
        }
    }

    def __init__(self, config, max_gas_price=-1, gas_price_level='standard'):
        # Required parameters: config = {'secret': ''}
        # additional config['network'] = mainnet or rinkeby
        # max_gas_price (wei) will prevent actions if gas price is too high
        # gas_price_level is a parameter from gnosis gas station API (see).

        self.logger = logging.getLogger('gnosis.extension')

        self.network = config.get('network', 'mainnet').lower()
        if self.network not in self._NETWORK_CONFIGS.keys():
            raise KeyError(
                f"Invalid network name. Network must be one of {list(self._NETWORK_CONFIGS.keys())}"
            )
        self._network_config = self._NETWORK_CONFIGS[self.network]

        self.secret = config.get('secret')
        self.account = Account.privateKeyToAccount(config.get('secret'))
        self.account_address = self.account.address
        self.web3 = Web3(Web3.WebsocketProvider(endpoint_uri=self._network_config['wss_url'], websocket_timeout=1800))

        self.logger.debug(f"Owner account: {self.account_address}")

        self.ALLOWED_TOKENS = self._network_config['allowed_tokens']

        self.dfusion_contract = DfusionContract(
            max_gas_price=max_gas_price,
            gas_price_level=gas_price_level,
            private_key=config.get('secret'),
            wss_url=self._network_config['wss_url'],
            contract_address=self._network_config['contract_address'],
            gnosis_gas_station_url=self._network_config['gnosis_gas_station_url'],
        )

        self.the_graph = TheGraph(self._network_config['thegraph_url'])
        self._load_tokens_info()

        self.logger.info(f"Current batch: {self.current_batch_id()}")

    def _load_tokens_info(self):
        # convert pairs to list of unique token names
        token_names = self.ALLOWED_TOKENS.keys()
        # Reverse lookup
        self._token_address_index = {}  # type: Dict[str, str]
        self._tokens = {}  # type: Dict[str, CryptoToken]

        tokens_info = self.the_graph.load_tokens_info(token_names)
        for token in tokens_info:
            if token.symbol in self.ALLOWED_TOKENS:
                if self.PRODUCTION and self.ALLOWED_TOKENS.get(token.symbol) != token.address:
                    raise UnknownTokenException(f"Token {token.symbol} address is incorrect")

            self._tokens[token.symbol] = token
            self._token_address_index[token.address] = token.symbol
            self.logger.debug(f"Loaded {token.symbol} dec {token.decimals} addr {token.address}")

        for symbol in token_names:
            if not self._tokens.get(symbol, False):
                raise TokenNotFoundException(symbol)

    def token(self, symbol) -> CryptoToken:
        return self._tokens[symbol]

    def token_by_address(self, address) -> CryptoToken:
        return self._tokens[self._token_address_index[address]]

    def get_web3(self) -> Web3:
        return self.web3

    def get_account(self) -> Account:
        return self.account

    def get_network_name(self) -> str:
        return self.network

    def get_wallet(self) -> str:
        return self.web3.toChecksumAddress(self.account.address)

    def get_network_config(self) -> Dict:
        return self._network_config
    # End of silly config methods

    def create_token_pair(self, symbol) -> TokenPair:
        return TokenPair(symbol, self._tokens)

    def fetch_my_trades(self, symbol, since: int, limit=1000):
        """
        This function returns list of EFrontier's trade objects for a specific symbol and
        orders placed by us.

        since is in milliseconds. Limit usually used with since.
        """

        token_pair = self.create_token_pair(symbol)

        since = int(since) // 1000

        results = self.the_graph.get_trades_by_owner(self.account_address, token_pair, trade_epoch_since=since)

        self.logger.info(f"Looking for trades {symbol} {since}")

        converted = []
        for raw_trade in results:
            try:
                if not raw_trade:
                    continue
                # Filter trades by token
                if (raw_trade.order.buy_token.symbol, raw_trade.order.sell_token.symbol) == \
                        (token_pair.base.symbol, token_pair.quote.symbol) or \
                        (raw_trade.order.sell_token.symbol, raw_trade.order.buy_token.symbol) == \
                        (token_pair.base.symbol, token_pair.quote.symbol):
                    trade = Trade.from_schema(token_pair, raw_trade)
                    converted.append(asdict(trade))

            except Exception as ex:
                self.logger.exception(ex)

        return converted

    def fetch_balance(self):
        """
        Returns a dictionary of the balances with following format
        { 'BTC': {'used': 1.5, 'free':2 'total': 3.5}, 'ETH': ..... }

        To calculate 'used' values we use currently open orders.
        'free' can be negative!

        """
        result = {}

        used = dict(zip(self._tokens.keys(), [0.0] * len(self._tokens.keys())))  # USDT: 0, BBBB: 0, etc.

        for pair in self.PAIRS:
            orders = self.fetch_open_orders(pair)
            for order in orders:
                token = order['info']['sell_token']  # dfusion has only sell orders.

                used[token] += order['info']['balance_used']

        for address in self._token_address_index.keys():
            balance = self.dfusion_contract.get_balance(address)
            ticker = self._token_address_index[address]
            token = self._tokens[ticker]

            result[ticker] = {'total': token.from_raw_amount(balance)}
            result[ticker]['used'] = used[ticker]
            result[ticker]['free'] = result[ticker]['total'] - result[ticker]['used']

        return result

    def cancel_order(self, order_id: int, symbol=None):
        """
        Cancels an order and returns a boolean indicating whether the cancellation was successful.
        """
        self.logger.info(f"Cancelling order {order_id}")
        tx_info = self.dfusion_contract.cancel_orders([int(order_id)])
        if tx_info.get('status', 0) == 0:
            return False
        else:
            return True

    def fetch_open_orders(self, symbol):
        """
        Returns a list of open orders for current batch
        """
        return self._fetch_open_orders(symbol, batch_id=self.current_batch_id())

    def _fetch_open_orders(self, symbol, batch_id):
        params = dict(owner=self.account_address, batch_id=batch_id, token_pair=self.create_token_pair(symbol))
        self.logger.debug(f"Fetching orders for {repr(params)}")
        orders = self.the_graph.fetch_open_orders(**params)

        contents = [asdict(Order.from_schema(order=order, token_pair=params['token_pair'])) for order in orders]
        contents.sort(key=lambda order: order['id'])

        return contents

    def fetch_orders_criteria(self, symbol, since: int, limit=1000):
        """
        since is in milliseconds
        """

        since = int(since // 1000)

        params = dict(owner=self.account_address, since=since, token_pair=self.create_token_pair(symbol), limit=limit)
        self.logger.debug(f"Fetching orders for {repr(params)}")

        orders = self.the_graph.fetch_orders(**params)

        contents = [asdict(Order.from_schema(order=order, token_pair=params['token_pair'])) for order in orders]
        contents.sort(key=lambda order: order['id'])

        return contents

    def fetch_order_book(self, symbol: str, depth=1000):
        """
        Returns the orderbook for a specific symbol from orders valid to this date.

        Orderbook is list of tradeable orders
        Example format {'asks': [(price,amount), (price,amount)] 'bids': [(price,amount), (price,amount)]}

        depth is ignored
        """

        def first(elem):
            return elem[0]

        batch_id = self.current_batch_id() - 1
        token_pair = self.create_token_pair(symbol)

        orders = self.the_graph.fetch_orderbook(token_pair=token_pair, batch_id=batch_id)

        contents = [Order.from_schema(order=order, token_pair=token_pair) for order in orders]

        result = {}  # of course we'll optimize it. Don't worry.

        result['asks'] = [(c.price, c.remaining) for c in contents if c.side == 'buy']
        result['bids'] = [(c.price, c.remaining) for c in contents if c.side == 'sell']

        result['asks'].sort(key=first)
        result['bids'].sort(key=first, reverse=True)

        return result

    def fetch_order(self, id: int, symbol: Optional[str] = None) -> dict:
        """
        Returns a single order object according to the ID.
        """
        token_pair = self.create_token_pair(symbol)
        order = self.the_graph.fetch_order(owner=self.account_address, order_id=id, token_pair=token_pair)
        order = Order.from_schema(order=order, token_pair=token_pair)
        return asdict(order) if order else []

    @staticmethod
    def _utctimestamp():
        return int(time.time())

    def _convert_to_gnosis_order(self, token_pair: TokenPair, side, volume, price, lifetime, valid_from):
        """
        Convert order data from ccxt to dfusion format

        to sell WETH/USDT : sell WETH receive USDT
        to buy WETH/USDT : sell USDT receive WETH

        valid_from: batch id
        lifetime: how many batches to live
        """

        params = {
            "buyToken": "",
            "sellToken": "",
            "validFrom": 0,
            "validUntil": 0,
            "buyAmount": "",
            "sellAmount": "",
        }

        if side == 'sell':
            params["sellToken"] = int(token_pair.base.id)
            params["buyToken"] = int(token_pair.quote.id)
            params["sellAmount"] = token_pair.base.to_raw_amount(volume)
            params["buyAmount"] = token_pair.quote.to_raw_amount(volume * price)
        if side == 'buy':
            params["sellToken"] = int(token_pair.quote.id)
            params["buyToken"] = int(token_pair.base.id)
            params["sellAmount"] = token_pair.quote.to_raw_amount(volume * price)
            params["buyAmount"] = token_pair.base.to_raw_amount(volume)

        params["validFrom"] = valid_from
        params["validUntil"] = valid_from + lifetime - 1

        return params

    def create_limit_sell_order(self, symbol, volume, price, lifetime=1):
        return self.create_limit_order(symbol, 'sell', volume, price, lifetime)

    def create_limit_buy_order(self, symbol, volume, price, lifetime=1):
        return self.create_limit_order(symbol, 'buy', volume, price, lifetime)

    def create_limit_order(self, symbol, side, volume, price, lifetime=1):
        """
        Note: Volume is in base currency.

        Orders are always placed as limit sell orders:
        sell up to “max sell amount” of SellToken for at least sell_amount/buy_amount.
        The limit price is implicitly calculated by the ratio of sell_amount and buy_amount.

        lifetime: how many batches to live (default 1 , i.e. current batch only)
        todo: replace lifetime with params as in binance extension

        The function is supposed to return order fetched back from thegraph.
        Due to sync timeout order info may not be available. The function will return empty data with only TX hash
        filled.
        """

        token_pair = self.create_token_pair(symbol)
        self.logger.info(f"Placing {side} order: {symbol} volume {volume} for {price}. Lifetime {lifetime} batch(es)")

        order_data = self._convert_to_gnosis_order(token_pair, side, volume, price,
                                               valid_from=self.current_batch_id(),
                                               lifetime=lifetime)

        tx = self.dfusion_contract.create_sell_order(**order_data)

        time.sleep(self.THEGRAPH_TIMEOUT)
        raw_orders = self.the_graph.fetch_orders_by_tx(tx.transactionHash.hex())

        orders = [asdict(Order.from_schema(order=order, token_pair=token_pair)) for order in raw_orders]
        orders.sort(key=lambda order: order['id'])

        if orders:
            return orders[0]
        else:
            self.logger.warning(f"Can't find order id for transaction {tx.transactionHash.hex()}")
            return {'info': {'txHash': tx.transactionHash.hex()}}

    def _convert_multiple_orders(self, orders: List[Order], current_batch, lifetime=1):
        order_batch = dict(
            buyToken=[],
            sellToken=[],
            buyAmount=[],
            sellAmount=[],
            validFrom=[],
            validUntil=[])

        for order in orders:
            self.logger.info(f"Placing {order.side} order: {order.symbol} volume {order.amount} for {order.price}")

            params = self._convert_to_gnosis_order(token_pair=self.create_token_pair(order.symbol),
                                                   side=order.side,
                                                   volume=order.amount,
                                                   price=order.price,
                                                   lifetime=lifetime,
                                                   valid_from=current_batch
                                                   )

            for key in order_batch.keys():
                order_batch[key].append(params[key])

        return order_batch

    def create_multiple_orders(self, orders: List[Order], current_batch, lifetime=1) -> List[dict]:
        order_batch = self._convert_multiple_orders(orders, current_batch, lifetime)

        result = self.dfusion_contract.create_multiple_sell_orders(**order_batch)

        raw_orders = self.the_graph.fetch_orders_by_tx(result.transactionHash.hex())

        time.sleep(self.THEGRAPH_TIMEOUT)
        orders = [asdict(Order.from_schema(order=raw_order, token_pair=self.create_token_pair(order.symbol))) for
                  raw_order in raw_orders]
        orders.sort(key=lambda order: order['id'])

        return orders

    def replace_multiple_orders(self, orders_to_cancel: List[int], orders: List[Order], current_batch, lifetime=1):
        order_batch = self._convert_multiple_orders(orders, current_batch, lifetime)
        if orders_to_cancel:
            order_batch['cancellations'] = orders_to_cancel
            result = self.dfusion_contract.replace_multiple_sell_orders(**order_batch)
        else:
            """Back to create if there's nothing to cancel"""
            result = self.dfusion_contract.create_multiple_sell_orders(**order_batch)

        time.sleep(self.THEGRAPH_TIMEOUT)
        raw_orders = self.the_graph.fetch_orders_by_tx(result.transactionHash.hex())

        orders = [asdict(Order.from_schema(order=order, token_pair=self.create_token_pair(order.symbol)))
                    for order in raw_orders]
        orders.sort(key=lambda order: order['id'])

        return orders

    def load_markets(self):
        """
        Does nothing. Function exists for compatibility with ccxt's API.
        """
        pass

    # Additional functions

    def current_batch_id(self) -> int:
        # b1 = self.dfusion_contract.get_current_batch_id()
        b2 = int(self._utctimestamp() / self.BATCH_SIZE)
        # self.logger.debug(f"SC batch id: {b1} calculated {b2}")
        return b2

    def batch_id_from_timestamp(self, ts: int) -> int:
        return int(ts / self.BATCH_SIZE)

    def seconds_remaining_in_batch(self) -> int:
        # s1 = self.dfusion_contract.get_seconds_remaining_in_batch()
        s1 = self._utctimestamp()
        return self.BATCH_SIZE - (s1 % self.BATCH_SIZE)

    def estimate_amount_at_price(self, symbol: str, side: str, volume: float, price: float) -> float:
        self.logger.info(f"Estimate amount: {side} {symbol} for {price} . Our volume: {volume}")
        token_pair = self.create_token_pair(symbol)

        if side == 'buy':
                            # buy               # sell
            market = f'{token_pair.base.id}-{token_pair.quote.id}'  # Sell USDC
            est_price = price

        elif side == 'sell':
                            # buy               # sell
            market = f'{token_pair.quote.id}-{token_pair.base.id}'  # Sell WETH
            est_price = 1/price  # inverted price
        else:
            raise ValueError()

        criteria = f"markets/{market}/estimated-amounts-at-price/{est_price}?atoms=false"

        self.logger.info(self._network_config['gnosis_price_estimator_url'] + criteria)
        response = requests.get(self._network_config['gnosis_price_estimator_url'] + criteria)

        estimated_volumes = response.json()

        buy_amount = float(estimated_volumes['buyAmountInBase'])
        sell_amount = float(estimated_volumes['sellAmountInQuote'])

        if side == 'buy':
            estimated_amount = buy_amount
        elif side == 'sell':
            estimated_amount = sell_amount

        self.logger.info(f"Estimated amount: we can {side} up to {estimated_amount} of {token_pair.symbol} at price {price}")

        return sell_amount


    def estimate_price_at_amount(self, symbol: str, side: str, volume: float, price: float) -> float:
        """

        The problem with this query is that it will give you the price
        if you really want to sell *all* of your 21.033 WETH in the current batch
         (this may incur a lot of slippage).

        """
        token_pair = self.create_token_pair(symbol)

        self.logger.info(f"Estimate price to {side} {volume} of {symbol}. Our price {price}")

        if side == 'sell':
            amount = volume
            market = f'{token_pair.quote.id}-{token_pair.base.id}'
        elif side == 'buy':
            amount = volume * price
            market = f'{token_pair.base.id}-{token_pair.quote.id}'
        else:
            raise ValueError()

        """
        Tokens: WETH: id=1 decimals=18    USDC: id=4  decimals=6

        buy 10 WETH/USDC for 1000

        sellAmount = 10,000
        
        Example 1. We want to sell  21.033 WETH/USDC for 238.98
        sellAmount = 21.033
        
        """
        criteria = f"markets/{market}/estimated-buy-amount/{amount}?atoms=false"
        response = requests.get(self._network_config['gnosis_price_estimator_url'] + criteria)
        self.logger.info(self._network_config['gnosis_price_estimator_url'] + criteria)

        estimation_data = response.json()
        assert str(amount) == estimation_data['sellAmountInQuote']

        estimated_amount = float(estimation_data['buyAmountInBase'])

        if side == 'buy':
            estimated_price = amount / estimated_amount
        elif side == 'sell':
            estimated_price = estimated_amount / amount


        self.logger.info(f"Estimated price: {estimated_price} to {side} {estimated_amount} of {token_pair.symbol}, (requested amount {volume} and price {price}")

        return estimated_price
        #


    def status(self):
        result = dict(
            utc=self._utctimestamp(),
            current_batch_id=self.current_batch_id(),
            remaining_time=self.seconds_remaining_in_batch(),
        )
        return result

    def __str__(self):
        return "gnosis"


class TheGraph:
    """
    Encapsulate GraphQL queries specific for dfusion
    """
    page_size = 1000

    def __init__(self, endpoint):
        self.logger = logging.getLogger('gnosis.extension.graph')
        self.endpoint = endpoint
        self.http_endpoint = HTTPEndpoint(endpoint)

    def _paginated(self, query):
        """
        Abstracts the fact that results are paginated.
        @author Marco
        """
        cur_page_size = self.page_size
        cur_skip = 0
        while cur_page_size == self.page_size:
            cur_page = query(skip=cur_skip)
            cur_page_size = len(cur_page)
            cur_skip += cur_page_size
            for i in cur_page:
                yield i

    def _get_orders_page(self, orders_filter, skip):
        op = Operation(schema.Query)
        orders = op.orders(
            where=orders_filter,
            skip=skip,
            first=self.page_size
        )
        orders.id()
        orders.order_id()
        orders.buy_token().symbol()
        orders.sell_token().symbol()
        orders.max_sell_amount()
        orders.price_numerator()
        orders.price_denominator()
        orders.owner().id()
        orders.from_epoch()
        orders.until_epoch()
        orders.cancel_epoch()
        orders.create_epoch()
        orders.delete_epoch()
        orders.from_batch_id()
        orders.until_batch_id()
        orders.bought_volume()
        orders.sold_volume()
        orders.tx_hash()

        data = self.http_endpoint(op)
        query = op + data
        return query.orders if hasattr(query, 'orders') else []

    def fetch_orderbook(self, token_pair, batch_id):
        return self._fetch_orders(token_pair, {'from_batch_id_lte': batch_id, 'until_batch_id_gte': batch_id})

    def fetch_orders(self, token_pair, **conditions):
        params = dict(from_epoch_gte=conditions['since'],
                      limit=conditions['limit'],
                      )

        return self._fetch_orders(token_pair, params)

    def fetch_open_orders(self, owner, token_pair, batch_id):
        # To know if it’s open,we must make sure we are within it’s validity range
        # (it can be checked by batch or date using: fromBatchId, untilBatchId, fromEpoch, untilEpoch)
        # todo: an open order is an order that still have "remaining" > 0 and is not cancelled...

        return self._fetch_orders(token_pair, {'owner': owner.lower(),
                                               'from_batch_id_lte': batch_id,
                                               'until_batch_id_gte': batch_id
                                               # 'from_epoch_lte': now,
                                               # 'until_epoch_gte': now
                                               })

    def _fetch_orders(self, token_pair, conditions: dict):
        """
        #
        # Make sure is not canceled or deleted (it shouldn’t have a date in  cancelEpoch, deleteEpoch)

        """

        orders_filter = {
            'buy_token_in': [token_pair.base.id, token_pair.quote.id],
            'sell_token_in': [token_pair.base.id, token_pair.quote.id],
            'delete_epoch': None,
            'cancel_epoch': None,
        }
        orders_filter.update(conditions)  # Join with custom conditions

        orders_generator = self._paginated(partial(self._get_orders_page, orders_filter))

        return orders_generator

    def fetch_order(self, owner: str, order_id: int, token_pair: TokenPair):
        orders_filter = {
            'order_id': order_id,
            'owner': owner.lower(),
        }
        result = self._get_orders_page(orders_filter, skip=0)
        if not result:
            raise OrderNotFound(str(order_id))

        return result[0]

    def fetch_orders_by_tx(self, tx_hash):
        orders_filter = {
            'tx_hash': tx_hash
        }
        orders_generator = self._paginated(partial(self._get_orders_page, orders_filter))
        return orders_generator

    def _get_trades_page(self, trades_filter, skip) -> List:
        op = Operation(schema.Query)
        trades = op.trades(
            where=trades_filter,
            skip=skip,
            first=self.page_size
        )
        trades.id()
        trades.owner().id()
        trades.buy_volume()
        trades.sell_volume()
        trades.order.buy_token().symbol()
        trades.order.sell_token().symbol()
        trades.order.order_id()
        trades.order.owner().id()
        trades.trade_epoch()
        trades.create_epoch()
        trades.trade_batch_id()
        data = self.http_endpoint(op)
        query = op + data
        return query.trades if hasattr(query, 'trades') else []

    def get_trades_by_owner(self, owner, token_pair, trade_epoch_since=0) -> Iterable:
        """
        Trade's owner.id is the same as order.owner.id according to Felix L.

        Notes:
        1. currently there is no filtering by token pair. We suppose that we always trade WETH/USDT.
        2. Reverted trades are still displayed

        {
            'id': id,
            'datetime': date,
            'price': price,
            'timestamp': timestamp,
            'amount': amount,
            'side': side,
            'symbol': ,
            'takerOrMaker': 'taker'
            'info': t,
        }
        """

        trades_filter = {}
        # Others can trade with our orders
        trades_filter["owner"] = owner.lower()
        # trades_filter["order_in"] = [order.id for order in orders]
        trades_filter["revert_epoch"] = None
        trades_filter['trade_epoch_gte'] = trade_epoch_since
        results = self._paginated(partial(self._get_trades_page, trades_filter))

        return results

    def load_tokens_info(self, tokens: List) -> List[CryptoToken]:
        op = Operation(schema.Query)
        tokens = op.tokens(
            where={"symbol_in": tokens}
        )
        tokens.id()
        tokens.address()
        tokens.decimals()
        tokens.symbol()
        tokens.name()

        data = self.http_endpoint(op)
        query = op + data
        result = query.tokens if hasattr(query, 'tokens') else []
        result = [CryptoToken.from_schema(token) for token in result]

        return result


class GnosisReportingExchange(GnosisExchange):
    """
    Supplies Chroniker KPI scripts with data.
    Methods in this extension return different data due to nature of Gnosis protocol.

    """

    def fetch_open_orders(self, symbol):
        """
        Returns a list of orders  for a specific symbol that were open in previous batch.
        """
        return super()._fetch_open_orders(symbol, batch_id=self.current_batch_id() - 1)

    def fetch_order_book(self, symbol: str, depth=1000):
        """
        In gnosis protocol we can encounter volumes that are too large for our DB.
        Gnosis utilities may even report such volumes as Infinite.
        As temporary measurement we replace Infinite / very large volumes to 0

        """
        result = super().fetch_order_book(symbol, depth)

        MAX_VALUE = 999999999999999  # Max size of our DB

        def f1(pair):
            return pair if pair[1] < MAX_VALUE else [pair[0], 0]

        result['asks'] = list(map(lambda x: f1(x), result['asks']))
        result['bids'] = list(map(lambda x: f1(x), result['bids']))

        return result


class DfusionContract:
    WEB3_TX_TIMEOUT = 240

    def __init__(self, private_key, wss_url=None, contract_address=None, **kwargs):
        self.logger = logging.getLogger('gnosis.extension.contract')
        self.web3 = Web3(Web3.WebsocketProvider(endpoint_uri=wss_url, websocket_timeout=1800))

        self.private_key = private_key
        self.account = Account.privateKeyToAccount(self.private_key)
        self.contract_address = self.web3.toChecksumAddress(contract_address)
        self.gnosis_gas_station_url = kwargs.get('gnosis_gas_station_url', 'https://safe-relay.rinkeby.gnosis.io/api/v1/gas-station/')

        abi_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'gnosis/exchange_abi.json')

        with open(abi_file) as json_file:
            abi = json.load(json_file)
            self.contract = self.web3.eth.contract(address=self.contract_address, abi=abi)

        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum network.")

        self.max_gas_price = kwargs.get('max_gas_price', -1)
        self.gas_price_level = kwargs.get('gas_price_level', 'standard')

    def get_seconds_remaining_in_batch(self):
        return self.contract.functions.getSecondsRemainingInBatch().call()

    def get_current_batch_id(self):
        return self.contract.functions.getCurrentBatchId().call()

    def get_balance(self, token_address):
        return self.contract.functions.getBalance(
            self.account.address,
            self.web3.toChecksumAddress(token_address)).call()

    def create_sell_order(self, buyToken: int, sellToken: int, buyAmount: int, sellAmount: int, validFrom=0,
                          validUntil=1):

        self.logger.info(f"New order: valid between {validFrom} and {validUntil} buyToken: {buyToken} sellToken: {sellToken} buyAmount: {buyAmount} sellAmount {sellAmount}")

        tx = self.contract.functions.placeOrder(
            buyToken,
            sellToken,
            validUntil,
            buyAmount,
            sellAmount) \
            .buildTransaction({
            'from': self.account.address,
            'gas': GAS_GNOSIS_ORDER,
            'gasPrice': self.get_gas_price(),
            'nonce': self.web3.eth.getTransactionCount(self.account.address)
        })

        return self._sign_and_send_and_wait_tx(tx)

    def get_contract(self):
        return self.contract

    def create_multiple_sell_orders(self,
                                    buyToken: List[int],
                                    sellToken: List[int],
                                    buyAmount: List[int],
                                    sellAmount: List[int],
                                    validFrom: List[int],  # batch id
                                    validUntil: List[int]  # batch id
                                    ) -> Hash32:

        balance = self.web3.fromWei(self.web3.eth.getBalance(self.account.address), 'ether')
        gas = len(buyAmount) * GAS_GNOSIS_BATCH_ORDER
        gas_price_wei = self.get_gas_price()

        tx = self.contract.functions.placeValidFromOrders(
            buyToken,
            sellToken,
            validFrom,
            validUntil,
            buyAmount,
            sellAmount
            ).buildTransaction({
                'from': self.account.address,
                'gasPrice': gas_price_wei,
                'nonce': self.web3.eth.getTransactionCount(self.account.address, 'pending'),
            })

        # BTW estimated gas is 96948 per order

        tx['gas'] = gas

        fee = self.web3.fromWei(gas * gas_price_wei, 'ether')

        if fee > balance:
            raise InsufficientFunds(f"Insufficient funds on account. Required: {fee} available: {balance} ETH")

        self.logger.info(f"Calling placeValidOrders. Transaction fee: {fee} ETH")

        return self._sign_and_send_and_wait_tx(tx)

    def replace_multiple_sell_orders(self,
                                    cancellations: List[int],
                                    buyToken: List[int],
                                    sellToken: List[int],
                                    buyAmount: List[int],
                                    sellAmount: List[int],
                                    validFrom: List[int],  # batch id
                                    validUntil: List[int]  # batch id
                                    ) -> Hash32:

        balance = self.web3.fromWei(self.web3.eth.getBalance(self.account.address), 'ether')
        gas = len(buyAmount) * GAS_GNOSIS_BATCH_ORDER + len(cancellations) * GAS_GNOSIS_CANCEL_ORDER
        gas_price_wei = self.get_gas_price()

        fee = self.web3.fromWei(gas * gas_price_wei, 'ether')

        if fee > balance:
            raise InsufficientFunds(f"Insufficient funds on account. Required: {fee} available: {balance} ETH")

        tx = self.contract.functions.replaceOrders(
            cancellations,
            buyToken,
            sellToken,
            validFrom,
            validUntil,
            buyAmount,
            sellAmount
            ).buildTransaction({
                'from': self.account.address,
                'gas': gas,
                'gasPrice': gas_price_wei,
                'nonce': self.web3.eth.getTransactionCount(self.account.address, 'pending'),
            })

        self.logger.info(f"Calling replaceOrders. Transaction fee: {fee} ETH")

        return self._sign_and_send_and_wait_tx(tx)

    def cancel_orders(self, order_ids):
        tx = self.contract.functions.cancelOrders(order_ids).buildTransaction({
            'from': self.account.address,
            'gas': GAS_GNOSIS_CANCEL_ORDER * len(order_ids),
            'gasPrice': self.get_gas_price(),
            'nonce': self.web3.eth.getTransactionCount(self.account.address, 'pending')
        })
        return self._sign_and_send_and_wait_tx(tx)

    def _sign_and_send_and_wait_tx(self, tx):
        signed = self.account.signTransaction(tx)
        tx_hash = self.web3.eth.sendRawTransaction(signed.rawTransaction)
        self.logger.info(f"Waiting for tx receipt on: {tx_hash.hex()}")

        x = self.web3.eth.waitForTransactionReceipt(transaction_hash=tx_hash, timeout=self.WEB3_TX_TIMEOUT)
        self.logger.info(f"Received tx receipt {tx_hash.hex()}")
        return x

    def get_account_address(self) -> str:
        return self.account.address

    def get_gas_price(self) -> int:
        """
        values for selector: lowest, safeLow, standard, fast, fastest
        """
        try:
            response = requests.get(self.gnosis_gas_station_url, params={'src': 'ef'})
            response.raise_for_status()
            results = response.json()
            price = int(results.get(self.gas_price_level))

        except requests.exceptions.RequestException as ex:
            price = self.web3.eth.gasPrice
            self.logger.warning(f"Error using gas station price API. Reverting to web3 price {price}. Exception: {str(ex)}")

        if self.max_gas_price != -1 and price >= self.max_gas_price:
            raise GasTooHigh(f"Gas price too high: {price}")

        self.logger.info(f"Gas price on {self.gas_price_level} is: {price} WEI")

        return price

    def create_filter(self, event_type, params=None):
        # 9340147 block # when the contract has been deployed
        # filter_builder = self.dfusion_contract.contract.events.Trade.buildFilter()
        # events = filter.get_all_entries()
        # for event in events:
        #     print(event)
        # fromBlock = 'latest'
        """
        See https://etherscan.io/address/0x6f400810b62df8e13fded51be75ff5393eaa841f#code
        for list of events

        event OrderPlacement(
            address indexed owner,
            uint16 index,
            uint16 indexed buyToken,
            uint16 indexed sellToken,
            uint32 validFrom,
            uint32 validUntil,
            uint128 priceNumerator,
            uint128 priceDenominator
        );
        event Trade(
        address indexed owner,
        uint16 indexed orderId,
        uint16 indexed sellToken,
        uint16 buyToken,
        uint128 executedSellAmount,
        uint128 executedBuyAmount
        );

        event TradeReversion(
            address indexed owner,
            uint16 indexed orderId,
            uint16 indexed sellToken,
            // Solidity only supports three indexed arguments
            uint16 buyToken,
            uint128 executedSellAmount,
            uint128 executedBuyAmount
        );
        """
        filter_params = dict(fromBlock='latest')
        if type(params) == dict:
            filter_params.update(params)

        if event_type == 'OrderPlacement':
            result = self.contract.events.OrderPlacement.createFilter(**filter_params)
        elif event_type == 'Trade':
            result = self.contract.events.Trade.createFilter(**filter_params)
        elif event_type == 'TradeReversion':
            result = self.contract.events.TradeReversion.createFilter(**filter_params)

        return result
