#
# Basket
#
import asyncio
import datetime
import os
from typing import Dict, Iterable, Union
from rateslib import BondFuture, FixedRateBond, dt
import requests
import yaml
import magic
from hashlib import md5
from stdnum import cusip as cu

from dlv.thttp import get
from .future import Future
from .treasury import Treasury

# type TreasuryDict = Dict[str, Treasury | None]

# python 3.9
TreasuryDict = Dict[str, Union[Treasury, None]]

__search_url__ = 'https://www.treasurydirect.gov/TA_WS/securities/search'

class Basket():
    def __init__(self, treasuries: TreasuryDict = {}):
        self.cusips: TreasuryDict = treasuries
        self._has_basket = False

    def has_basket(self) -> bool:
        return self._has_basket

    @property
    def future(self):
        return self.future
    
    @future.setter
    def future(self, value: str):
        self._future = Future.parse(value)
        
    def build_from_yaml(self, treasuryYaml: dict):
        self._has_basket = False
        try:
            for key in treasuryYaml:
                if key == 'future':
                    self.future = treasuryYaml[key]
                    continue

                if not cu.is_valid(key):
                    raise ValueError('Bad cusip was given.')

                item = treasuryYaml[key]
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

                self.cusips[key] = treasury
                self._has_basket = True
        except Exception as e:
            self._has_basket = False

    async def build_from_text(self, treasuryText: Iterable) -> None:
        self._has_basket = False
        self.cusips = {}

        responses = await get(treasuryText)

        for response in responses:
            # response = requests.get(self.get_url(cusip))
            if response is None:
                continue

            if response.status_code != 200:
                continue

            data = response.json()

            if len(data) == 0:
                continue

            # Find the first non reopening entry
            for item in data:
                if item['reopening'] == 'Yes':
                    continue
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

                self.cusips[item['cusip']] = treasury
                self._has_basket = True

    def get(self, key: str) -> Union[Treasury, None]:
        return self.cusips.get(key)

    def get_future(self) -> Future:
        return self._future

    def hashcode(self) -> str:
        keys = '|'.join(self.cusips.keys())
        return md5(keys.encode()).hexdigest()

    @classmethod
    def from_file(cls, filename: str):
        _, tail = os.path.splitext(filename)

        tail = tail.lower()

        isTextFile = tail in ['', '.txt']
        isYamlFile = tail in ['.yml', '.yaml']

        if isTextFile:
            return Basket.read_from_text(filename)
        
        if isYamlFile:
            return Basket.read_from_yaml(filename)

        return None
    
    @classmethod
    def read_from_text(cls, filename):
        try:
            with open(filename, 'r') as f:
                text = f.read()
                lines = [t.strip() for t in text.splitlines()]
                dictionary = dict.fromkeys(lines)
                basket = cls(Future.parse(''))
                # await basket.build_from_text(dictionary)
                return basket
        except Exception as e:
            raise e

    @classmethod
    def read_from_yaml(cls, filename):
        basket = cls()
        with open(filename, 'r') as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            basket.build_from_yaml(yml)

        return basket

    def get_url(self, cusip) -> str:
        return __search_url__ + f'?cusip={cusip}&format=json' 
    
    def set_cusips(self, cusips: TreasuryDict):
        self.cusips = cusips
    
    def print(self):
        if not self.has_basket():
            raise ValueError('No available tresuries in basket')

        basket = [t.get_treasury() for t in self.cusips.values()] # type: ignore
        future = BondFuture(
            coupon=6.0,
            delivery=(dt(2024, 3, 1), dt(2024, 3, 28)),
            basket=basket, # type: ignore
            nominal=100e3,
            calendar="nyc",
            currency="usd",
            # calc_mode='ust_short',
            calc_mode='ust_long'
        )

        prices = [t.price if not t is None else 0 for t in self.cusips.values()]
        df = future.dlv(
            future_price=130 + (27/32),
            prices=prices,
            repo_rate=5.32,
            settlement=dt(2024,1,5),
            # delivery=dt(2024,3,28),
            convention='Act360',
        )

        # 0.5980
        # 0.8281
        # usbf.basket
        print(df)

    @classmethod
    def unserialize(cls, filename): 
        return cls.from_file(filename)

    def serialize(self) -> str:
        strYaml = ''
        for cusip in self.cusips:
            treasury = self.cusips.get(cusip)
            if treasury is None:
                continue

            strYaml += (treasury.to_yaml(cusip) + '\n\n')

        if not self._future is None:
            strYaml = f'future: {self._future.long_code}\n\n' + strYaml


        return strYaml