#
# dlv:future
#
import re
from rateslib import get_calendar

from .enums import FutureMonths, TreasuryFutures

__invalid_future_message__ = 'Not a valid future code given. Must be one of TU, FV, Z3N, TY, TN, TWE, US, UL'
__invalid_contract_month__ = 'Invalid contract month given. Only H,M,U and Z are valid.'

class Future:
    def __init__(self):
        self._month = 0
        self._year = 0
        self._tenor = 0
        self._code = ''
        
    def month(self) -> int:
        return self._month

    def year(self):
        return self._year

    def set_year(self, value: int):
        self._year = value
        return self
    
    def set_month(self, value: int):
        self._month = value
        return self
    
    def set_code(self, value: str):
        self._code = value.upper()
        return self
    
    def set_tenor(self, value: int):
        self._tenor = value
        return self
    
    def short_name(self) -> str:
        return self._code + FutureMonths(self._month).name + str(self._year)[-1]
        
    def get_month_code(self) -> str:
        return FutureMonths(self._month).name

    def get_tenor(self) -> int:
        return self._tenor

    def get_deliveries(self):
        cal =  get_calendar('nyc')
        holidays = cal.

    def __hash__(self):
        strRepr = str(self)
        return hash(strRepr)

    def __str__(self) -> str:
        return self._code + FutureMonths(self._month).name + str(self._year)

    @staticmethod
    def parse(name: str):
        m = re.match('(\\w{2})(\\w{1})(\\d{1,4})$', name)

        if m is None:
            raise ValueError(__invalid_future_message__)
        
        if len(m.groups()) != 3: # type: ignore
            raise ValueError(__invalid_future_message__)

        tenor = 0    
        try:
            tenor = TreasuryFutures[m.group(1).upper()]
        except Exception as e:
            raise e

        month = 0
        try:
            month = FutureMonths[m.group(2).upper()]
        except Exception as e:
            raise e
        
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
            
        future = Future()
        future.set_code(tenor.name).set_tenor(tenor.value).set_year(futureYear).set_month(month.value)

        return future