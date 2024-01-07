#
# dlv:tests:basket 
#
import pytest
from dlv.basket import Basket

@pytest.fixture
def generate_cusips():
    return [
        '9128286Y1',
        '912828XW5',
        '9128287C8',
        '9128282P4',
        '912828YA2',
        '9128282S8',
        '912828YF1',
        '9128282W9',
    ]

def test_hash_code(generate_cusips: list[str]):
    tr = {t:None for t in generate_cusips}
    basket = Basket(tr) # type:ignore
    hash = basket.hashcode()
    assert len(hash) == 32