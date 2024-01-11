#
# dlv:future
#
from dataclasses import dataclass
import re
from rateslib import get_calendar
from typing import Final
from .enums import FutureMonths, TreasuryFutures

NOTIONAL_COUPON: Final = 6.0

__invalid_future_message__ = 'Not a valid future code given. Must be one of TU, FV, Z3N, TY, TN, TWE, US, UL'
__invalid_contract_month__ = 'Invalid contract month given. Only H, M, U and Z are valid.'

@dataclass(frozen=True)
class Future:
    code: str
    tenor: int
    month: int
    year: int

    @property
    def short_code(self) -> str:
        return '' if self.is_empty else \
            self.code + FutureMonths(self.month).name + str(self.year)[-1]
        
    @property
    def median_code(self) -> str:
        return '' if self.is_empty else \
            self.code + FutureMonths(self.month).name + str(self.year)[-2]

    @property
    def long_code(self) -> str:
        return '' if self.is_empty else str(self)

    @property
    def month_code(self) -> str:
        return '' if self.is_empty else FutureMonths(self.month).name

    @property
    def is_empty(self):
        return self.year == 0 and self.month == 0 and self.tenor == 0 and self.code == '' 

    def get_deliveries(self):
        cal =  get_calendar('nyc')
        # holidays = cal.

    def __hash__(self):
        strRepr = str(self)
        return hash(strRepr)

    def __str__(self) -> str:
        if self.is_empty: return ''
        return self.code + FutureMonths(self.month).name + str(self.year)

    @classmethod
    def parse(cls, name: str):
        m = re.match('(\\w{2})(\\w{1})(\\d{1,4})$', name)

        if m is None:
            return Future('', 0, 0, 0)
            # raise ValueError(__invalid_future_message__)
        
        if len(m.groups()) != 3: # type: ignore
            raise ValueError(__invalid_future_message__)

        tenor = 0    
        try:
            tenor = TreasuryFutures[m.group(1).upper()]
        except KeyError as e:
            raise ValueError(__invalid_future_message__) from None

        month = 0
        try:
            month = FutureMonths[m.group(2).upper()]
        except Exception as e:
            raise ValueError(__invalid_contract_month__) from None

        if not month.name in ['H', 'M', 'U', 'Z']:
            raise ValueError(__invalid_contract_month__)

        length = len(m.group(3)) if not m.group(3) is None else 0

        if length == 4:
            futureYear = int(m.group(3))
        elif length == 2:
            futureYear = 2000 + int(m.group(3))
        elif length == 1:
            futureYear = 2020 + int(m.group(3))
        else:
            futureYear = 0
            
        return cls(tenor.name, tenor.value, month.value, futureYear)