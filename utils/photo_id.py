from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram import Bot, Dispatcher, types
from class_table_check import *
from config import API_TOKEN, PROXY_URL

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class_id = {'c01': '7А', 'c02': '7Б', 'c03': '7В', 'c04': '7Г', 'c05': '8А', 'c06': '8Б БМ', 'c07': '8Б ФХ',
            'c08': '8В', 'c09': '8Г', 'c10': '8Д', 'c11': '9А ФМ', 'c12': '9А МИ', 'c13': '9Б', 'c14': '9В',
            'c15': '9Г', 'c16': '9Д', 'c17': '10А ФМ', 'c18': '10А МЭ', 'c19': '10Б', 'c20': '10В БМ', 'c21': '10В ГУМ',
            'c22': '11А', 'c23': '11Б', 'c24': '11В МИ', 'c25': '11В БМ', 'c26': '11Г', 'c27': '11Д'}
final = {}
ids = list(class_id.keys())
ph_ids = []


@dp.message_handler(content_types=['photo'])
async def id_photo(message: types.message):
    ph_ids.append(message.photo[0].file_id)
    await message.answer('got it')


@dp.message_handler(commands=['set'])
async def saving(message: types.Message):
    for i in range(0, 26):
        final[ids[i]] = ph_ids[i]
    print(final)
    await message.answer('successful')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())