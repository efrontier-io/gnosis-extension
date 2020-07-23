from extensions import gnosis_extension as df_ext
import pytest


def setup_module():
    global token_pair, additional_args

    symbol = 'WETH/USDC'
    tokens_info = dict(
        WETH=df_ext.CryptoToken(1, None, 'Test Wrapped ETH', 'WETH', 18),
        USDC=df_ext.CryptoToken(4, None, 'Test USDC', 'USDC', 6),
    )
    token_pair = df_ext.TokenPair(symbol, tokens_info)
    additional_args = dict(
        valid_from=int(df_ext.GnosisExchange._utctimestamp() / df_ext.GnosisExchange.BATCH_SIZE),
        lifetime=1
    )

def test_order_build():
    """Test that we correctly pass data in ccxt format to dfusion"""
    global token_pair, additional_args

    # Place an order to sell
    side = 'sell'
    volume = 1000
    price = 250

    params = df_ext.GnosisExchange._convert_to_gnosis_order(
                                                             token_pair, side, volume, price,                                                              additional_args['lifetime'],
                                                             additional_args['lifetime'],
                                                             additional_args['valid_from']        )
    print(params)

    assert params['sellToken'] == token_pair['WETH'].id
    assert params['buyToken'] == token_pair['USDC'].id
    assert params['sellAmount'] == 1000000000000000000000
    assert params['buyAmount'] == 250000000000

    side = 'buy'
    volume = 1000
    price = 250

    params = df_ext.GnosisExchange._convert_to_gnosis_order(token_pair, side, volume, price,
                                                            additional_args['lifetime'],
                                                            additional_args['valid_from'])

    assert params['sellToken'] == token_pair['USDC'].id
    assert params['buyToken'] == token_pair['WETH'].id
    assert params['sellAmount'] == 250000 * 10**6
    assert params['buyAmount'] == 1000 * 10**18

