#
# dlv:tests:cache
#

from io import StringIO
import pytest
from dlv.basket import Basket
from dlv.cache import Cache
from .basket_fixture import create_basket

def test_cache_basket(create_basket: Basket, mocker):
    basket = create_basket
    c = Cache(basket=basket)
    mo =  mocker.patch("builtins.open")
    r =  c.put()
    assert r

    # c.cache_basket(basket)