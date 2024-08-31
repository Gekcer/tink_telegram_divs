import pandas as pd
import pytest

@pytest.fixture
def prepare_df():
    df = pd.read_csv('check.csv')
    return df

def parse_dividend(row):
    stock_name_string = f'Название акции: {row["stock_name"]}\n'
    currency_string = f'Валюта: {row["currency"]}\n'
    figi_string = f'Номер FIGI: {row["figi"]}\n'
    last_buy_date_string = f'Дата последней закупки для дивидендов: {row["last_buy_date"][:10]}\n{10*"-"}'
    text = stock_name_string + currency_string + figi_string + last_buy_date_string
    return text

def test_parse_dividend(prepare_df):
    example_df = prepare_df[0:1]
    assert type(example_df) == type(pd.DataFrame())

    list_of_strings = [parse_dividend(row) for index, row in example_df.iterrows()]
    record_string = '\n'.join(list_of_strings)
    print('\n\n')
    print(record_string)

