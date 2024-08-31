import asyncio
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.environ.get('TELEGRAM_TOKEN')

# Конфиг
MESSAGEMAXLENGTH = 4096 # максимальная длина сообщения

# Датафрейм дивидендов
div_df = pd.read_csv('../check.csv')

# Бот и диспетчер
bot = Bot(token=telegram_token)
dp = Dispatcher()

def parse_dividend(row):
    stock_name_string = f'Название акции: {row["stock_name"]}\n'
    currency_string = f'Валюта: {row["currency"]}\n'
    figi_string = f'Номер FIGI: {row["figi"]}\n'
    last_buy_date_string = f'Дата последней закупки для дивидендов: {row["last_buy_date"][:10]}\n{10*"-"}'
    text = stock_name_string + currency_string + figi_string + last_buy_date_string
    return text

def get_record_string(df):
    list_of_strings = [parse_dividend(row) for index, row in df.iterrows()]
    record_string = '\n'.join(list_of_strings)
    return record_string

async def get_messages(message, record_string):
    if len(record_string) > MESSAGEMAXLENGTH:
        chunks = [record_string[i:i+4096] for i in range(0, len(record_string), MESSAGEMAXLENGTH)]
        for chunk in chunks:
            await message.answer(chunk)
    else:
        await message.answer(record_string)

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

@dp.message(Command('show_all'))
async def cmd_show_all_divs(message: types.Message):
    record_string = get_record_string(div_df)
    # if len(record_string) > MESSAGEMAXLENGTH:
    #     chunks = [record_string[i:i+4096] for i in range(0, len(record_string), MESSAGEMAXLENGTH)]
    #     for chunk in chunks:
    #         await message.answer(chunk)
    # else:
    #     await message.answer(record_string)
    await get_messages(message, record_string)

@dp.message(Command('show_filtered'))
async def cmd_show_filtered(
        message: types.Message,
        command: CommandObject
):
    if command.args is None:
        await message.answer(
            'Ошибка ввода команды.\nПример: /show_filtered <валюта>'
        )
        return
    currency = command.args
    filtered_df = div_df.copy(deep=True)
    filtered_df = filtered_df[filtered_df['currency'] == currency]
    record_string = get_record_string(filtered_df)
    await get_messages(message, record_string)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
