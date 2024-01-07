#
# dlv:tests:basket 
#
import pytest
from dlv.basket import Basket
from .basket_fixture import create_basket

def test_hash_code(create_basket):
    basket = create_basket
    hash = basket.hashcode()
    assert len(hash) == 32