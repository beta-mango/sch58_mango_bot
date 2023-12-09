from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram import Bot, Dispatcher, types
#from config import API_TOKEN, PROXY_URL

storage = MemoryStorage()
bot = Bot(token='5948532687:AAGv17ff0EQPXZH6ce6g6VjtAbOVOKK9k58')
dp = Dispatcher(bot, storage=storage)


class_id = {'c01': '6А', 'c02': '6Б', 'c03': '7А', 'c04': '7Б', 'c05': '7В', 'c06': '8А', 'c07': '8Б',
            'c08': '8В ФМ', 'c09': '8В МЭ', 'c10': '8Г', 'c11': '9А', 'c12': '9Б ФХ', 'c13': '9Б БМ', 'c14': '9В',
            'c15': '9Г', 'c16': '9Д', 'c17': '10А ФМ', 'c18': '10А БМ', 'c19': '10Б', 'c20': '10В МИ', 'c21': '10В ГУМ',
            'c22': '10Г', 'c23': '11А ФМ', 'c24': '11А МЭ', 'c25': '11Б', 'c26': '11В БМ', 'c27': '11В ГУМ'}
final = {}
ids = list(class_id.keys())
ph_ids = []


@dp.message_handler(content_types=['photo'])
async def id_photo(message: types.message):
    ph_ids.append(message.photo[0].file_id)
    print(message.photo[0].file_id)


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