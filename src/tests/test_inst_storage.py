import pytest

class InstrumentStorage:
    def __init__(self):
        self.instruments = []

    def append_instrument(self, instrument):
        self.instruments.append(instrument)
        return self

    def __iter__(self):
        return iter(self.instruments)

    def __getitem__(self, item):
        return self.instruments[item]


def test_if_storage_is_iterable():
    inst_s = InstrumentStorage()
    inst_s.append_instrument('stock1')
    inst_s.append_instrument('stock2')

    assert inst_s[0] == 'stock1'
    assert inst_s[1] == 'stock2'