from div_observer.dividend_observer import DividendObserver
from div_observer.storage_manager import StorageManager
from instrument_storage.instrument_storage import InstrumentStorage

if __name__ == '__main__':
    storage = InstrumentStorage()
    div_obs = DividendObserver(storage)

    # div_obs.form_instrument_storage()
    # # print(len(div_obs.storage_manager.storage))
    # stor = div_obs.storage_manager.storage
    # example_stock = stor[1]
    # figi0 = example_stock.figi
    # example_dividend = div_obs.get_dividends(figi0)
    #
    # print(f'Информация об акции {figi0} из хранилища:\n {example_stock}\n')
    # print(f'Информация о дивидендах: \n {example_dividend}')

    div_obs.work()
