#
# dlv:tests:quote
#
import pytest
from dlv.quote import Quote, QuoteStyle

@pytest.mark.parametrize(
    "value, style, expected",
    [
        ('108\'18\'2', QuoteStyle.DETECT, 108.5703125),
        ('103\'03\'3', QuoteStyle.SHORT_NOTE_FUTURE, 103.10546875),
        ('110.11', QuoteStyle.DETECT, 110.11),
        ('110', QuoteStyle.DETECT, 110),
        ('110-11', QuoteStyle.NOTE_FUTURE, 110.34375),
        ('103-253', QuoteStyle.BOND, 103.792968750),
        ('tum4', QuoteStyle.BOND, 0),
    ]
)
def test_qoute_parse(value, style, expected):
    q = Quote.parse(value, style)
    assert q.price == expected