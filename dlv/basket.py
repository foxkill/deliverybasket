#
# Basket
#
import datetime
import os
from typing import Dict, Union
from rateslib import FixedRateBond, dt
import requests
import yaml
import magic

from . import Treasury

# type TreasuryDict = Dict[str, Treasury | None]

# python 3.9
TreasuryDict = Dict[str, Union[Treasury, None]]

__search_url__ = 'https://www.treasurydirect.gov/TA_WS/securities/search'

class Basket():
    def __init__(self, treasuries: TreasuryDict = {}):
        self.cusips: TreasuryDict = treasuries

    def build_from_yaml(self, treasuryYaml: dict):
        for cusip in treasuryYaml:
            item = treasuryYaml[cusip]
            issueDate = item['effective']
            maturityDate = item['termination']
            
            eff = dt(issueDate.year, issueDate.month, issueDate.day)
            mat = dt(maturityDate.year, maturityDate.month, maturityDate.day)

            frb = FixedRateBond(
                effective=eff,
                termination=mat,
                fixed_rate=item['fixed_rate'],
                spec='ust'
            )

            treasury = Treasury(
                treasury=frb, 
                effective=eff, 
                termination=mat,
                price=item['price'],
                fixed_rate=item['fixed_rate']
            )

            self.cusips[cusip] = treasury

    def build_from_text(self) -> TreasuryDict:
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

            treasury = Treasury(
                treasury=frb, 
                effective=eff, 
                termination=mat,
                price=0,
                fixed_rate=rate
            )

            self.cusips[cusip] = treasury

        return self.cusips

    def get(self, key: str) -> Union[Treasury, None]:
        return self.cusips.get(key)

    @staticmethod
    def from_file(filename: str):
        head, tail = os.path.splitext(filename)

        tail = tail.lower()

        isTextFile = tail in ['', '.txt']
        isYamlFile = tail in ['.yml', '.yaml']

        if isTextFile:
            basket = Basket()
            cusips = basket.read_from_text(filename)
            basket.set_cusips(cusips)
            basket.build_from_text()
            return basket
        
        if isYamlFile:
            basket = Basket()
            yml = basket.read_from_yaml(filename)
            basket.build_from_yaml(yml)
            return basket

        return None
    
    @staticmethod
    def read_from_text(filename):
        with open(filename, 'r') as f:
            text = f.read()
            return dict.fromkeys(text.splitlines())

    @staticmethod
    def read_from_yaml(filename):
        with open(filename, 'r') as file:
            return yaml.load(file, Loader=yaml.SafeLoader)

    def get_url(self, cusip) -> str:
        return __search_url__ + f'?cusip={cusip}&format=json' 
    
    def set_cusips(self, cusips: TreasuryDict):
        self.cusips = cusips
    
    def serialize(self, filename) -> bool:
        head, tail = os.path.splitext(filename)

        if not tail.lower() in ['.yml', '.yaml']:
            filename = head + tail + '.yaml'
           
        strYaml = ''
        for cusip in self.cusips:
            treasury = self.cusips.get(cusip)
            if treasury is None:
                continue

            strYaml += (treasury.to_yaml(cusip) + '\n\n')

        if len(strYaml) == 0:
            return False

        with open(filename, 'w+') as f:
            f.write(strYaml)

        return True


