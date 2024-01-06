#
# dlv:tests
#
from dlv.enums import FutureMonths


def test_monthcodes():
    assert 'June' == FutureMonths.M.value