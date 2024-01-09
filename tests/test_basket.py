#
# dlv:tests:basket 
#
import pytest
import pytest_asyncio
import requests_mock
from unittest.mock import mock_open, patch
from datetime import datetime
from dlv.basket import Basket, __search_url__
from .basket_fixture import create_basket, response_for_912810TV0

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
def get_treasury_dict():
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

@pytest.mark.asyncio
async def test_build_read_from_text(create_future, response_for_912810TV0):
    with patch('dlv.basket.open', mock_open(read_data=' \t912810TV0\n')) as mo:
        with requests_mock.Mocker() as mock:
            mock.get(__search_url__, json=response_for_912810TV0)
            basket = Basket.read_from_text('basket.txt')
            assert not basket is None
            assert basket.has_basket() == True

def test_build_from_text(create_future, response_for_912810TV0):
    treasuryDict = { '912810TV0': None }
    basket = Basket(create_future)
    with requests_mock.Mocker() as mock:
        mock.get(__search_url__, json=response_for_912810TV0)
        basket.build_from_text(treasuryDict) # type: ignore
        assert basket.has_basket() == True
    
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