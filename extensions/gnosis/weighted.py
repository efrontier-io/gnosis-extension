import logging
from .errors import NotEnoughOffersOrderbookException


def middle_price(book) -> float:
    if len(book['asks'])>0 and len(book['bids'])>0:
        return (book['asks'][0][0] + book['bids'][0][0]) / 2
    else:
        raise NotEnoughOffersOrderbookException("can not calculate mid_price")


def weighted_average(funds, offers):
    """
    Given "amount" of US$ to spend,
    calculate weighted avg price of 1 ETH to purchase

    amount: US$ to grab from the orderbook
    offers: list of prices from the orderbook
    """
    total_shares = 0
    total_amount = 0
    pos = 0

    while funds > 0:
        try:
            price_level, quantity = offers[pos]
        except IndexError as ex:
            raise NotEnoughOffersOrderbookException(funds)

        position_amount = price_level*quantity
        if funds >= position_amount:
            total_shares += quantity
            total_amount += position_amount
            funds -= position_amount
            logging.debug(f"Position: {pos} funds: {funds} offer: ETH {price_level} / {quantity} ({position_amount} USD) Shares aquired: {total_shares} ")

        else:
            new_quantity = funds / price_level
            total_shares += new_quantity
            total_amount += funds
            funds = 0
            logging.debug(f"Position: {pos} funds: {funds} offer:  {price_level} ETH/USDT. Shares aquired: {total_shares} New quantity: {new_quantity} USD)")

        pos += 1

    return total_amount/total_shares
