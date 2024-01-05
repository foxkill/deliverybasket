#
# dlv:treasury
#
from rateslib import FixedRateBond, dt

class Treasury():
    def __init__(self, 
                 treasury: FixedRateBond, 
                 effective: dt, 
                 termination: dt,
                 fixed_rate: float,
                 price: float
                ):
        self.termination = termination
        self.fixed_rate = fixed_rate
        self.effective = effective
        self.treasury = treasury
        self.price = price
    
    def get_price(self) -> float:
        return self.price
    
    def get_termination(self) -> dt:
        return self.termination
    
    def get_effective(self) -> dt: 
        return self.effective
    
    def get_treasury(self) -> FixedRateBond:
        return self.treasury

    def get_fixed_rate(self) -> float:
        return self.fixed_rate
    
    def to_yaml(self, cusip) -> str:
        price = self.get_price()
        effective = self.get_effective().strftime('%Y-%m-%dT%H:%M:%S')
        termination =  self.get_termination().strftime('%Y-%m-%dT%H:%M:%S')
        fixed_rate = self.get_fixed_rate()

        return f'{cusip}:\n  effective: {effective}\n  termination: {termination}\n  price: {price}\n  fixed_rate: {fixed_rate}'
