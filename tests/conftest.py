#
# dlv:tests:conftest
#
import pytest

from dlv.future import Future

@pytest.fixture(autouse=True, name="generate_cusips")
def generate_cusips():
    return [
        '9128286Y1',
        '912828XW5',
        '9128287C8',
        '9128282P4',
        '912828YA2',
        '9128282S8',
        '912828YF1',
        '9128282W9',
    ]

@pytest.fixture(autouse=True)
def create_future() -> Future:
    return Future.parse('ulh4')