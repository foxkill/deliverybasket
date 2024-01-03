#
# Basket
#
from typing import List
from rateslib import FixedRateBond

from . import Treasury

class Basket():
    def __init__(self):
        self.cusips = []

    def add(self, cusip: str) -> None:
        self.cusips.append(cusip)

    def get(self) -> List[Treasury]:
        if len(self.cusips) == 0:
            return []
        return []

    def from_file(self, filename: str) -> List[Treasury]:
        cusips = ''
        with open(filename, 'r') as f:
            cusips = f.read()
        
        self.cusips = cusips.splitlines()
        return []