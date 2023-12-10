from PIL import Image, ImageDraw, ImageFont
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from utils.kb_markups import *
from processing import *
import datetime


class UserState(StatesGroup):
    br_entering = State()
    lunch_entering = State()
    date_entering = State()


storage = MemoryStorage()
bot = Bot(token='6408066558:AAG6AxVGXj8_Ki3OxmPTITal_e9HnLsdhQE')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def started(message: types.Message):
    await message.answer('Enter /br to start')


@dp.message_handler(commands=['br'])
async def br_started(message: types.Message, state: FSMContext):
    await message.answer('Enter all the br meals with a comma')
    await UserState.br_entering.set()


@dp.message_handler(content_types=['text'], state=UserState.br_entering)
async def br_meals(message: types.Message, state: FSMContext):
    breakfast_meals = message.text.split('. ')
    vert = add_breakfast(breakfast_meals)
    async with state.proxy() as data:
        data['y'] = vert
    await UserState.lunch_entering.set()
    await message.answer('Enter all the lunch meals with a comma')


@dp.message_handler(content_types=['text'], state=UserState.lunch_entering)
async def lunch(message: types.Message, state: FSMContext):
    lunch_meals = message.text.split('. ')
    async with state.proxy() as data:
        l_vert = data['y']
    s_number = add_dinner(lunch_meals, l_vert)
    if s_number == 0:
        await message.answer('Lunch meals added. Enter the date')
    await UserState.date_entering.set()


@dp.message_handler(content_types=['text'], state=UserState.date_entering)
async def date(message: types.Message, state: FSMContext):
    f_number = add_date(message.text)
    if f_number == 0:
        photo = open('backg1.png', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await message.answer('Done')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, timeout=60, skip_updates=True)

