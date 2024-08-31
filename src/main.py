from div_observer.dividend_observer import DividendObserver
from div_observer.storage_manager import StorageManager
from instrument_storage.instrument_storage import InstrumentStorage

def prepare_dividend_record():
    storage = InstrumentStorage()
    div_obs = DividendObserver(storage)
    div_obs.work()

if __name__ == '__main__':
    # storage = InstrumentStorage()
    # div_obs = DividendObserver(storage)
    # div_obs.form_instrument_storage()
    prepare_dividend_record()
