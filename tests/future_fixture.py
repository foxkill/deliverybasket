#
# dlv:tests:fixture:future
#
import pytest
from dlv.future import Future

@pytest.fixture
def create_future() -> Future:
    return Future.parse('ulh4')