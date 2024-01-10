#
# dlv:http
# 
from typing import Iterable
import httpx as requests
import asyncio

__search_url__ = 'https://www.treasurydirect.gov/TA_WS/securities/search'

async def fetch(url):
    await asyncio.sleep(1/1000)
    return requests.get(url)

async def get(cusips: Iterable[str]):
    urls = [url(cusip) for cusip in cusips]
    responses = await asyncio.gather(*[fetch(url) for url in urls])
    return responses

def url(cusip):
    return __search_url__ + f'?cusip={cusip}&format=json' 