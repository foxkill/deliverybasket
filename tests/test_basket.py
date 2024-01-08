#
# dlv:tests:basket 
#
import pytest
from datetime import datetime
from dlv.basket import Basket
from .basket_fixture import create_basket

@pytest.fixture
def generate_bad_treasury_dict():
    return {
        'future': 'ulh2024', 
        '912810SH2': {
            'effective': datetime.strptime('2019-05-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'termination': datetime.strptime('2049-05-15T00:00:00','%Y-%m-%dT%H:%M:%S'),
            'price': 77.53,
            'fixed_rate': 2.87
        },
        '912810TV': {
            'effective': datetime.strptime('2023-11-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'termination': datetime.strptime('2053-11-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'price': 109.2334,
            'fixed_rate': 4.75,
        },
        '912810TV0': {
        }
    }

@pytest.fixture
def get_treasury_dict(generate_cusips):
    cusips = generate_cusips
    return {
        'future': 'ulh2024', 
        '912810SH2': {
            'effective': datetime.strptime('2019-05-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'termination': datetime.strptime('2049-05-15T00:00:00','%Y-%m-%dT%H:%M:%S'),
            'price': 77.53,
            'fixed_rate': 2.87
        },
        '912810TV0': {
            'effective': datetime.strptime('2023-11-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'termination': datetime.strptime('2053-11-15T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'price': 109.2334,
            'fixed_rate': 4.75,
        }
    }

def test_build_from_yaml(get_treasury_dict, create_future):
    basket = Basket(create_future) 
    basket.build_from_yaml(get_treasury_dict)
    assert basket.has_basket() == True

def test_build_from_yaml_with_bad_entries(generate_bad_treasury_dict, create_future):
    basket = Basket(create_future) 
    basket.build_from_yaml(generate_bad_treasury_dict)
    assert basket.has_basket() == False

def test_build_from_yaml_with_empty_dict( create_future):
    basket = Basket(create_future) 
    basket.build_from_yaml({})
    assert basket.has_basket() == False


def test_hash_code(create_basket):
    basket = create_basket
    hash = basket.hashcode()
    assert len(hash) == 32