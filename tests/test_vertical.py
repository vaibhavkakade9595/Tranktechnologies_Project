
import pytest
from pages.vertical import vertical


def test_trading(page):
    trading_obj=vertical(page)
    trading_obj.Trading_options_clicking()
    