#
# dlv
#
from rateslib import FixedRateBond


class Treasury():
    def __init__(self, treasury: FixedRateBond, price: float):
        self.tresury = treasury
        self.price = price
    
    def get_price(self) -> float:
        return self.price
    
    def get_treasury(self) -> FixedRateBond:
        return self.tresury