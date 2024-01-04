#
# Basket
#
import datetime
from typing import Dict, Union
from rateslib import FixedRateBond, dt
import requests

from . import Treasury

# type TreasuryDict = Dict[str, Treasury | None]

# python 3.9
TreasuryDict = Dict[str, Union[Treasury, None]]

__search_url__ = 'https://www.treasurydirect.gov/TA_WS/securities/search'

class Basket():
    def __init__(self):
        self.cusips: TreasuryDict = {}

    # def add(self, cusip: str) -> None:
    #     self.cusips.append(cusip)

    def build(self) -> TreasuryDict:
        if len(self.cusips) == 0:
            return {}
        
        for cusip in self.cusips:
            response = requests.get(self.get_url(cusip))

            if response.status_code != 200:
                return {}

            data = response.json()

            if len(data) == 0:
                return {}

            item = data[0]

            issueDate = datetime.datetime.strptime(item['issueDate'], '%Y-%m-%dT%H:%M:%S')
            maturityDate = datetime.datetime.strptime(item['maturityDate'], '%Y-%m-%dT%H:%M:%S')
            
            eff = dt(issueDate.year, issueDate.month, issueDate.day)
            mat = dt(maturityDate.year, maturityDate.month, maturityDate.day)

            rate = float(item['interestRate'])

            frb = FixedRateBond(
                effective=eff,
                termination=mat,
                fixed_rate=rate,
                spec='ust'
            )

            treasury = Treasury(frb, 0)

            self.cusips[cusip] = treasury

        return self.cusips

    def from_file(self, filename: str) -> TreasuryDict:
        text = ''
        with open(filename, 'r') as f:
            text = f.read()
        
        self.cusips = dict.fromkeys(text.splitlines())

        return self.build()

    def get_url(self, cusip) -> str:
        return __search_url__ + f'?cusip={cusip}&format=json' 
