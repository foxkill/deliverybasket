#
# dlv:quote
#
from dataclasses import dataclass
import enum

import re
from typing import Final

class QuoteStyle(enum.IntFlag):
    DETECT = 0
    BOND = 1
    SHORT_NOTE_FUTURE = 3
    NOTE_FUTURE = 4
    BOND_FUTURE = 5
    DECIMAL = 6

FRACTION32_BOND: Final = {
    0: 0,
    1: 1/8,
    2: 1/4,
    3: 3/8,
    4: 1/2,
    5: 5/8,
    6: 3/4,
    7: 7/8
}

FRACTION32_NOTE: Final = {
    2: 1/4,
    5: 1/2,
    7: 3/4
}

FRACTION32_SHORT_TERM_NOTE = {
    1: 1/32/8,
    2: 2/32/8,
    3: 3/32/8,
    4: 4/32/8,
    5: 5/32/8,
    6: 6/32/8,
    7: 8/32/8,
}

def parse_short_term_note_future_price(number: str, fraction: str, fraction32: str) -> float:
    """Parse the price of a note future, TN, ZN, ZF, ZT"""
    price = 0
    if number.isnumeric():
        price += int(number)

    if fraction32.isnumeric() and not (fraction32.isnumeric() or fraction32 != '+'):
        price += (float(fraction) / 32)
    else:    
        fraction_index = int(fraction32)

        debug =  FRACTION32_SHORT_TERM_NOTE.get(fraction_index, 0)
        price += \
            (int(fraction)/32) + \
            FRACTION32_SHORT_TERM_NOTE.get(fraction_index, 0)

    return price


def parse_note_future_price(number: str, fraction: str, fraction32: str) -> float:
    """Parse the price of a note future, TN, ZN, ZF, ZT"""
    price = 0
    if number.isnumeric():
        price += int(number)

    if fraction32.isnumeric() and not (fraction32.isnumeric() or fraction32 != '+'):
        price += (float(fraction) / 32)
    else:    
        fraction_index = '0'

        if fraction32 == '+':
            fraction_index = '5'

        fraction_index = int(fraction32)

        price += \
            (int(fraction) + \
            FRACTION32_NOTE.get(fraction_index, 0))/32

    return price

def parse_bond_future_price(number: str, fraction: str, fraction32: str) -> float:
    price = 0

    if not number is None:
        price += int(number)

    if not fraction is None:
        price += (float(fraction) / 32)

    return price

def parse_tresury_price(number: str, fraction: str, fraction32: str) -> float:
    """Parse the price of a treasury bond, note etc."""
    price = 0

    if number.isnumeric():
        price += int(number)

    if fraction32.isnumeric() and not (fraction32.isnumeric() or fraction32 != '+'):
        price += (float(fraction) / 32)
    else:    
        fraction_index = '0'

        if fraction32 == '+':
            fraction_index = '4'

        fraction_index = int(fraction32)

        price += \
            (int(fraction) + \
            FRACTION32_BOND.get(fraction_index, 0))/32

    return price

def parse_decimal(number: str, fraction: str, fraction32: str) -> float:
    price_str = '%s.%s%s' % (number, fraction, fraction32)
    return float(price_str)

def parse_none(number: str, fraction: str, fraction32: str) -> float:
    return 0

def detect_quote_style(delimiter_frac: str, delimiter32: str) -> QuoteStyle:
    if not delimiter_frac is None and delimiter_frac == '.':
        return QuoteStyle.DECIMAL
    if (not delimiter_frac is None and delimiter_frac == "'"):
        if (not delimiter32 is None and delimiter32 == "'"):
            return QuoteStyle.NOTE_FUTURE
        else:
            return QuoteStyle.BOND_FUTURE

    return QuoteStyle.BOND

PARSER: Final = {
    QuoteStyle.BOND: parse_tresury_price,
    QuoteStyle.BOND_FUTURE: parse_bond_future_price,
    QuoteStyle.NOTE_FUTURE: parse_note_future_price,
    QuoteStyle.SHORT_NOTE_FUTURE: parse_short_term_note_future_price,
    QuoteStyle.DECIMAL: parse_decimal,
}

@dataclass
class Quote:
    price: float

    @classmethod
    def parse(cls, quote: str, quotestyle = QuoteStyle.DETECT):
        price = 0
        regex = r"(?P<number>^\d+)(?P<delimiter_frac>[\.\-\'])?(?P<fraction>\d{2})?(?P<delimiter32>'?)(?P<fraction32>\d\+)?"
        matches = re.finditer(regex, quote, re.MULTILINE)

        for matchnum, match in enumerate(matches, start=1):
            number = match.group('number')
            fraction =  match.group('fraction') 
            fraction32 = match.group('fraction32')

            style = quotestyle if quotestyle != QuoteStyle.DETECT else \
                detect_quote_style(match.group('delimiter_frac'), match.group('delimiter32'))

            number = '0' if number is None else number
            fraction = '0' if fraction is None else fraction
            fraction32 = '0' if fraction32 is None else fraction32

            fn = PARSER.get(style, parse_none)
            price = fn(number, fraction, fraction32)
            break

        return cls(price)