#
# dlv:tests:quote
#
import pytest

from dlv.quote import Quote, QuoteStyle, detect_quote_style


@pytest.mark.parametrize(
    "value, style, expected",
    [
        ('103-04+', QuoteStyle.DETECT, 103.140625),
        ('97-186', QuoteStyle.BOND, 97.5859375),
        ('97-187', QuoteStyle.DETECT, 97.5859375),
        ('103\'03\'3', QuoteStyle.SHORT_NOTE_FUTURE, 103.10546875),
        ('110.11', QuoteStyle.DETECT, 110.11),
        ('110', QuoteStyle.DETECT, 110),
        ('110-11', QuoteStyle.NOTE_FUTURE, 110.34375),
        ('103-253', QuoteStyle.BOND, 103.792968750),
        ('tum4', QuoteStyle.BOND, 0),
    ]
)
def test_quote_parse(value, style, expected):
    q = Quote.parse(value, style)
    assert q.price == expected

@pytest.mark.parametrize(
    "fraction32, delimiter_frac, delimiter32, expected",
    [
        (None, None, None, QuoteStyle.BOND), # Default
        ('', '', '', QuoteStyle.BOND), # Default
        ('325', '.', None, QuoteStyle.DECIMAL), # Decimal
        ('+', '', '', QuoteStyle.BOND), # 108-04+
        ('2', '\'', '', QuoteStyle.BOND_FUTURE), # 108'181
    ]
)
def test_detect_quote_style(fraction32, delimiter_frac, delimiter32, expected):
    result = detect_quote_style(fraction32, delimiter_frac, delimiter32)
    assert result == expected