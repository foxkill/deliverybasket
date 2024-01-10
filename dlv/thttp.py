#
# dlv:http
# 
from typing import Final, Iterable
import httpx as requests
import asyncio

TIMEOUT = 10
MAX_CONNECTIONS = 8

__search_url__: Final = 'https://www.treasurydirect.gov/TA_WS/securities/search'

async def fetch(client, url):
    return client.get(url)

async def get(cusips: Iterable[str]) -> list[requests.Response]:
    client = requests.Client(timeout=TIMEOUT, limits=requests.Limits(max_connections=MAX_CONNECTIONS))
    responses = await asyncio.gather(*[fetch(client, url(cusip)) for cusip in cusips])
    return responses

def url(cusip):
    return __search_url__ + f'?cusip={cusip}&format=json' 