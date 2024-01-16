#
# dlv:tests:treasury
# test for the treasury object
#

import datetime

import pytest
from rateslib import FixedRateBond

from dlv.treasury import Treasury, TreasuryType


@pytest.fixture
def bond() -> FixedRateBond:
    frb = FixedRateBond(
        termination=datetime.datetime(2025, 1, 1),
        effective=datetime.datetime(2020, 1, 1),
        fixed_rate=4+(1/8),
        spec='ust'
    )
    return frb

@pytest.fixture
def treasury(bond) -> Treasury:
    t = Treasury(
        termination=datetime.datetime(2025, 1, 1),
        effective=datetime.datetime(2020, 1, 1),
        treasury=bond,
        fixed_rate=2.5,
        type=TreasuryType.BOND,
        price=103+((3/8)/32)
    )
    return t

def test_to_yaml(treasury, generate_cusips):
    cusip = generate_cusips[0]
    t = treasury

    yaml = t.to_yaml_ex(cusip)

    assert cusip in yaml
    assert '2020-01-01T00:00:00' in yaml
    assert '2025-01-01T00:00:00' in yaml
    assert '2.5' in yaml
    assert f'{103+((3/8)/32)}' in yaml
    assert f'{TreasuryType.BOND.value}' in yaml

def test_to_yaml_with_invalid_cusip(treasury, generate_cusips):
    cusip = 'xvii'
    t = treasury
    with pytest.raises(ValueError):
       assert t.to_yaml(cusip)