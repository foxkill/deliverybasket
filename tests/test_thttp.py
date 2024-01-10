#
# dlv:tests:thttp
#
import pytest
from dlv.thttp import get

@pytest.mark.asyncio
async def test_get_cusips(generate_cusips):
    cusips = [generate_cusips for i in range(8)]
    r = await get(cusips)
    assert len(r) == 8