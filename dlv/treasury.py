#
# dlv:treasury
#
import enum
from dataclasses import dataclass, field
from datetime import datetime

from rateslib import FixedRateBond, dt
from stdnum import cusip as cu


class TreasuryType(enum.Enum):
    NOTE = 'Note'
    BOND = 'Bond'

@dataclass(frozen=False)
class Treasury:
    termination: datetime
    fixed_rate: float
    effective: datetime
    treasury: FixedRateBond
    type: TreasuryType
    price: float

    def to_yaml(self, cusip: str) -> str:
        if not isinstance(cusip, str) or not cu.is_valid(cusip):
            raise ValueError(f'Invalid cusip number: {cusip} given')        

        yprice = self.price
        yeffective = self.effective.strftime('%Y-%m-%dT%H:%M:%S')
        ytermination =  self.termination.strftime('%Y-%m-%dT%H:%M:%S')
        yfixed_rate = self.fixed_rate

        return f'{cusip}:\n  effective: {yeffective}\n  termination: {ytermination}\n  price: {yprice}\n  fixed_rate: {yfixed_rate}'
