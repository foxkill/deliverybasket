#
# dlv:tests:thttp
#
import pytest
from dlv.thttp import get

NUMER_OF_CUSIPS = 2

@pytest.mark.asyncio
async def test_get_cusips(generate_cusips):
    cusips = generate_cusips[0:NUMER_OF_CUSIPS]
    r = await get(cusips)
    codes = list(filter(lambda x: (x.status_code == 200), r))
    assert len(r) == NUMER_OF_CUSIPS
    assert len(codes) == NUMER_OF_CUSIPS