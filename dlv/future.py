#
# dlv:future
#
from dataclasses import InitVar, dataclass, field
import datetime
import re
from calendar import monthrange 
from rateslib.calendars import _is_eom, _is_som, _is_holiday, get_calendar, CustomBusinessDay
from typing import Final, Optional, Union
from .enums import FutureMonths, TreasuryFutures

NOTIONAL_COUPON: Final = 6.0

__invalid_future_message__ = 'Not a valid future code given. Must be one of TU, FV, Z3N, TY, TN, TWE, US, UL'
__invalid_contract_month__ = 'Invalid contract month given. Only H, M, U and Z are valid.'

@dataclass(frozen=True, repr=False)
class Future:
    code: str
    tenor: int
    month: int
    year: int
    cal: Union[CustomBusinessDay, tuple[CustomBusinessDay, str]] = field(
        init=False
    )
    
    # UB, UBE, TWE, ZB, TN, ZN
    # first position day - 2 days before first delivery day in delivery month.
    # last position day - 2 days before last delivery day in delivery month
    # ZT, Z3N, ZF 
    # first positon - 2 days before FDD
    # last position - 1 BD after contract delivery month.
    @property
    def last_delivery_day(self) -> datetime.date:
        """The last_delivery_day property."""
        lastday = monthrange(self.year, self.month)[1]
        dt = datetime.datetime(self.year, self.month, lastday)
        mcal = get_calendar('nyc')
        for _ in range(lastday, -1, -1):
            if _is_holiday(dt, mcal) == False: # type: ignore
                break
            dt -= datetime.timedelta(days = 1)

        return dt.date()
        
    @property
    def first_delivery_day(self) -> datetime.date:
        """Get the first delivery day of the future contract"""
        mcal = get_calendar('nyc')
        dt = datetime.datetime(self.year, self.month, 1)
        lastday = monthrange(self.year, self.month)[1]
        for _ in range(lastday):
            result = _is_holiday(dt, mcal) # type: ignore
            if result == False:
                break
            dt += datetime.timedelta(days=1)

        return dt.date()

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
        
        if len(m.groups()) != 3: # type: ignore
            raise ValueError(__invalid_future_message__)

        tenor = 0    
        try:
            tenor_str = m.group(1).upper()
            tenor = TreasuryFutures[tenor_str]
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