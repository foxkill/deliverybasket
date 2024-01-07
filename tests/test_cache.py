#
# dlv:tests:cache
#

from dlv.basket import Basket
from dlv.cache import Cache
from dlv.future import Future

from .basket_fixture import create_basket
from .future_fixture import create_future

def test_cache_basket(create_future: Future, create_basket: Basket):
    future = create_future
    basket = create_basket
    c = Cache(future=future, basket=basket)
    assert c.put()

    # c.cache_basket(basket)