import pandas as pd


class RecordFormer:
    def __init__(self):
        self.record_df = pd.DataFrame(
            columns = [
                'stock_name',
                'currency',
                'figi',
                'last_buy_date',
                'data_date',
                'close_price',
                'yield_value',
                'dividend_net'
            ]
        )

    def add_record(self, record):
        self.record_df.loc[len(self.record_df)] = record
        return self

    def save_csv(self):
        self.record_df.to_csv('check.csv', index=False)
        return self
