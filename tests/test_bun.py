import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name_returns_correct_name(self, bun_data):
        name, price = bun_data
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price_returns_correct_price(self, bun_data):
        name, price = bun_data
        bun = Bun(name, price)
        assert bun.get_price() == price
        assert isinstance(bun.get_price(), float)