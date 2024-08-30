import os
import pytest

from dotenv import load_dotenv
from tinkoff.invest import Client, InstrumentIdType

load_dotenv()

@pytest.fixture
def token():
    return os.environ.get('TOKEN')

class DividendObserver:
    def __init__(self):
        self.set_token()

    def set_token(self):
        token = os.environ.get('TOKEN')
        if token is None:
            raise ValueError('Token is None')
        self.token = token

    def get_dividends_info(self):
        pass


def test_token(token):
    div_ob = DividendObserver()
    assert div_ob.token != None
    assert div_ob.token == token

def test_token_is_none():
    os.environ.pop('TOKEN', None)

    with pytest.raises(Exception) as e:
        div_ob = DividendObserver()

    assert str(e.value) == 'Token is None'
