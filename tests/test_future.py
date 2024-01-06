#
# dlv:tests:future
#
import pytest
from dlv.future import Future, __invalid_contract_month__, __invalid_future_message__

def test_parse():
    f = Future.parse('ulh4')
    assert f.month() == 3
    assert f.year() == 2024

def test_str():
    f = Future.parse('tuu2')
    assert str(f) == 'TUU2022'

def test_shortname(): 
    f = Future.parse('tNm3')
    assert f.short_name() == 'TNM3'

def test_get_month_code():
    f = Future.parse('TNH4')
    assert f.get_month_code() == 'H'

def test_get_tenor():
    ty = Future.parse('TYH4')
    tn = Future.parse('TNH4')
    assert ty.get_tenor() == 10
    assert tn.get_tenor() > 10

def test_accept_only_valid_contract_months():
    with pytest.raises(ValueError, match=__invalid_contract_month__):
        ty = Future.parse('TYF4')

def test_raise_error_if_garbage_string_is_given():
    with pytest.raises(ValueError, match=__invalid_future_message__):
        f = Future.parse('tuM1_')
