#
# dlv:treasury
#
from dataclasses import dataclass
from rateslib import FixedRateBond, dt
from datetime import datetime

@dataclass(frozen=False)
class Treasury:
    termination: datetime
    fixed_rate: float
    effective: datetime
    treasury: FixedRateBond
    price: float

    def to_yaml(self, cusip: str) -> str:
        yprice = self.price
        yeffective = self.effective.strftime('%Y-%m-%dT%H:%M:%S')
        ytermination =  self.termination.strftime('%Y-%m-%dT%H:%M:%S')
        yfixed_rate = self.fixed_rate

        return f'{cusip}:\n  effective: {yeffective}\n  termination: {ytermination}\n  price: {yprice}\n  fixed_rate: {yfixed_rate}'
