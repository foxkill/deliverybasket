#
# dlv:tests:basket:fixture
#
import pytest

from dlv.basket import Basket

@pytest.fixture
def create_basket(generate_cusips) -> Basket:
    tr = {t:None for t in generate_cusips}
    basket = Basket(tr) # type:ignore
    return basket