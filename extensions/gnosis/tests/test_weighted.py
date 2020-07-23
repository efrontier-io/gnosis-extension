from ..weighted import weighted_average
import pandas as pd
import numpy as np
import pytest
from ..errors import NotEnoughOffersOrderbookException

def test1():
    """Simple weighted average"""
    orderbook = [[300, 20], [200, 100], [150, 225]]
    df = pd.DataFrame(orderbook)
    weighted = np.average(df[0], weights=df[1])
    assert round(weighted, 2) == 173.19


def test2():
    """Weighted average of purchased options according to given funds"""
    orderbook = [[300, 20], [200, 100], [150, 225]]
    avg = weighted_average(funds=300 * 20 + 200 * 100 + 150 * 225, offers=orderbook)

    df = pd.DataFrame(orderbook)
    weighted = np.average(df[0], weights=df[1])

    assert avg == weighted

    ###
    avg2 = weighted_average(6000, orderbook)
    assert avg2 == 300

    with pytest.raises(NotEnoughOffersOrderbookException):
        avg3 = weighted_average(6000000, orderbook)
