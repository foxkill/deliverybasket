#
# dlv:tests:cache
#

from io import StringIO
from unittest.mock import mock_open, patch
import pytest
from dlv.basket import Basket
from dlv.cache import Cache
from .basket_fixture import create_basket

# def test_open(mocker):
#     m = mocker.patch('builtins.open', mocker.mock_open(read_data='bibble'))
#     with open('foo') as h:
#         result = h.read()

#     m.assert_called_once_with('foo')
#     assert result == 'bibble'

def test_cache_put(create_basket: Basket, mocker):
    basket = create_basket
    c = Cache()

    with patch('dlv.cache.open') as mo:
        out = mo()
        mo.side_effect = [out]
        r =  c.put(basket)
        assert r == True
        assert out.mock_calls[1].args[0].strip() == 'future: ' + basket.future.long_code

def test_cache_get(create_future):
    c = Cache()
    with patch('dlv.basket.open', mock_open(read_data='future: ulh2024')) as mo:
        basket = c.get(c.get_filename(create_future.long_code))
        assert not basket is None
        assert basket.get_future().long_code == 'ULH2024'
        assert basket.has_basket() == False

def test_cache_get_with_invalid_filename():
    c = Cache()
    filename = 'x'
    basket = c.get(filename)
    assert basket is None
