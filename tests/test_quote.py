#
# dlv:tests:quote
#
import pytest
from dlv.quote import Quote, QuoteStyle

@pytest.mark.parametrize(
    "value, style, expected",
    [
        ('110.11', QuoteStyle.DETECT, 110.11),
        ('110-11', QuoteStyle.NOTE_FUTURE, 110.34375),
        ('103-257', QuoteStyle.BOND, 103.80859375),
        ('tum4', QuoteStyle.BOND, 0),
    ]
)
def test_qoute_parse(value, style, expected):
    q = Quote.parse(value, style)
    assert q.price == expected