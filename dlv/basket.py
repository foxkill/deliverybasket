#
# Basket
#
import asyncio
import datetime
import os
from httpx import Response
from typing import Dict, Iterable, Union
from rateslib import BondFuture, FixedRateBond, dt
import yaml
from hashlib import md5
from stdnum import cusip as cu
from .thttp import get
from .future import Future, NOTIONAL_COUPON
from .treasury import Treasury

# python 3.9
TreasuryDict = Dict[str, Union[Treasury, None]]

class Basket():
    def __init__(self, treasuries: TreasuryDict = {}):
        self._cusips: TreasuryDict = treasuries
        self._has_basket = False
        self._future = Future.parse('')

    def has_basket(self) -> bool:
        return self._has_basket

    @property
    def future(self) -> Future:
        return self._future
    
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

                self._cusips[key] = treasury
                self._has_basket = True
        except Exception as e:
            self._has_basket = False

    async def build_from_responses(self, responses: Iterable[Response]):
        self._has_basket = False
        for response in responses:
            if response is None or response.status_code != 200:
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

                # usB = FixedRateBond(
                #     effective=dt(1990, 4, 2), termination=dt(1992, 3, 31),
                #     frequency="S", convention="ActActICMA", calc_mode="UST_31bii",
                #     fixed_rate=8.5, calendar="nyc", ex_div=1, modifier="none",
                # )

                frb = FixedRateBond(
                    effective=eff,
                    termination=mat,
                    fixed_rate=rate,
                    spec='ust'
                )

                # price=item.get('pricePer100', 100)
                treasury = Treasury(
                    treasury=frb, 
                    effective=eff, 
                    termination=mat,
                    price=100,
                    fixed_rate=rate
                )

                self._cusips[item['cusip']] = treasury
                self._has_basket = True

    async def build(self):
        self._has_basket = False
        responses = await get(self._cusips.keys())
        await self.build_from_responses(responses)    
        return self

    def get(self, key: str) -> Union[Treasury, None]:
        return self._cusips.get(key)

    def hashcode(self) -> str:
        keys = '|'.join(self._cusips.keys())
        return md5(keys.encode()).hexdigest()

    @classmethod
    def from_file(cls, filename: str):
        """Read a basket from a either a text fiel or yaml file"""
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
        with open(filename, 'r') as f:
            text = f.read()
            lines = [t.strip() for t in text.splitlines()]
            dictionary = dict.fromkeys(lines)
            return cls(dictionary)

    @classmethod
    def read_from_yaml(cls, filename):
        basket = cls()
        with open(filename, 'r') as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            basket.build_from_yaml(yml)

        return basket

    def set_cusips(self, cusips: TreasuryDict):
        self._cusips = cusips
    
    def get_calculation_mode(self) -> str:
        return 'ust_long'
    
    def get_settlement_date(self, settlement: str) -> datetime.date:
        return datetime.datetime.now() \
            if len(settlement) == '' else \
                datetime.datetime.strptime(settlement, '%Y-%m-%d')
    
    def print(self, future_price: float, repo_rate: float, settlement: str = ''):
        if not self.has_basket():
            raise ValueError('No available tresuries in basket.')

        date = self.get_settlement_date(settlement=settlement)
        basket = [t.get_treasury() for t in self._cusips.values()] # type: ignore

        # TODO: if we have notes, then we must set calc_mode to ust_short.
        future = BondFuture(
            coupon=NOTIONAL_COUPON,
            delivery=(dt(2024, 3, 1), dt(2024, 3, 28)),
            basket=basket, # type: ignore
            calendar="nyc",
            currency="usd",
            calc_mode=self.get_calculation_mode()
        )

        prices = [t.price if not t is None else 0 for t in self._cusips.values()]
        df = future.dlv(
            future_price=future_price,
            prices=prices,
            repo_rate=repo_rate,
            settlement=dt(date.year, date.month, date.day),
            convention='Act360',
        )

        print(df)

    @classmethod
    def unserialize(cls, filename): 
        return cls.from_file(filename)

    def serialize(self) -> str:
        strYaml = ''
        for cusip in self._cusips:
            treasury = self._cusips.get(cusip)
            if treasury is None:
                continue

            strYaml += (treasury.to_yaml(cusip) + '\n\n')

        if not self._future.is_empty:
            return f'future: {self._future.long_code}\n\n{strYaml}'

        return strYaml