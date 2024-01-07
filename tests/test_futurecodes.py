#
# dlv:tests
#
from dlv.enums import FutureMonths

def test_monthcodes():
    assert 6 == FutureMonths.M.value