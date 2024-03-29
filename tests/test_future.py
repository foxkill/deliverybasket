#
# dlv:tests:future
#
import datetime as dt
import pytest
from dlv.future import Future, __invalid_contract_month__, __invalid_future_message__

def test_parse():
    f = Future.parse('ulh4')
    assert f.month == 3
    assert f.year == 2024

def test_get_first_delivery_day_for_short_tenors():
    f = Future.parse('fvm2')
    assert f.get_first_delivery_day() == dt.datetime(2022, 6, 1)

@pytest.mark.parametrize(
    "future, expected",
    [
        ('tuh4', dt.datetime(2024, 4, 3)),
        ('tum4', dt.datetime(2024,  7, 3)),
        ('tuu4', dt.datetime(2024,  10, 3)),
        ('fvm2', dt.datetime(2022, 7, 6)),
        ('tnh4', dt.datetime(2024, 3, 28)),
        ('ulh4', dt.datetime(2024, 3, 28)),
    ]
)
def test_get_last_delivery_day_for_short_tenors(future, expected):
    f = Future.parse(future)
    assert f.get_last_delivery_day() == expected

def test_get_first_delivery_day_for_long_tenors():
    f = Future.parse('ulm2')
    assert f.get_first_delivery_day() == dt.datetime(2022, 6, 1)

def test_get_last_delivery_day_for_long_tenors():
    f = Future.parse('ulm2')
    assert f.get_last_delivery_day() == dt.datetime(2022, 6, 30)

def test_str_representation():
    f = Future.parse('tuu0')
    assert str(f) == 'TUU2020'

def test_shortname(): 
    f = Future.parse('tNm3')
    assert f.short_code == 'TNM3'

def test_get_month_code():
    f = Future.parse('TNH4')
    assert f.month_code == 'H'

def test_hash_code():
    f1  = Future.parse('TNH4')
    f2  = Future.parse('TNH4')
    assert hash(f1) == hash(f2)

def test_get_tenor():
    ty = Future.parse('TYH4')
    tn = Future.parse('TNH4')
    assert ty.tenor == 10
    assert tn.tenor > 10

def test_accept_only_valid_contract_months():
    with pytest.raises(ValueError, match=__invalid_contract_month__):
        ty = Future.parse('TYF4')

def test_raise_error_if_garbage_string_is_given():
    with pytest.raises(ValueError, match=__invalid_future_message__):
        f = Future.parse('uhl4')
