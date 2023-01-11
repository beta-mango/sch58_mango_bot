from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram import Bot, Dispatcher, types
from class_table_check import *
from config import API_TOKEN, PROXY_URL

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    choosing_class = State()
    typing_subs = State()
    sending = State()
    typing_subs_stream = State()
    other_ttable = State()
    other_act = State()
    changing_class = State()
    first_time = State()

class_id = {'c01': '7А', 'c02': '7Б', 'c03': '7В', 'c04': '7Г', 'c05': '8А', 'c06': '8Б БМ', 'c07': '8Б ФХ',
            'c08': '8В', 'c09': '8Г', 'c10': '8Д', 'c11': '9А ФМ', 'c12': '9А МИ', 'c13': '9Б', 'c14': '9В',
            'c15': '9Г', 'c16': '9Д', 'c17': '10А ФМ', 'c18': '10А МЭ', 'c19': '10Б', 'c20': '10В БМ', 'c21': '10В ГУМ',
            'c22': '11А', 'c23': '11Б', 'c24': '11В МИ', 'c25': '11В БМ', 'c26': '11Г', 'c27': '11Д'}
checker = class_id.values()
days = {'Понедельник': 'monday', 'Вторник': 'tuesday', 'Среда': 'wednesday', 'Четверг': 'thursday', 'Пятница': 'friday'}
checking = list(days.keys())
a = ' '

checker3 = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", 'Фото\U0001F4F8']
checker4 = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Фото расписания\U0001F4F8",
            "Расписание другого класса", "Галя, отмена!", "Посмотреть замены\U0001F440",
            "Изменить любимый класс\U0001F504", "Вернуться в меню\U0001F3E0", "Назад", "Выбор класса"]
class_stream = ['7', '8', '9', '10', '11']
seven = ['c01', 'c02', 'c03', 'c04']
eight = ['c05', 'c06', 'c07', 'c08', 'c09', 'c10']
nine = ['c11', 'c12', 'c13', 'c14', 'c15']
ten = ['c17', 'c18', 'c19', 'c20']
eleven = ['c22', 'c23', 'c24', 'c25', 'c26']
stream_id = {'7': seven, '8': eight, '9': nine, '10': ten, '11': eleven}


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    is_in_db = False
    user_id = str(message.from_user.id)
    user_id_class = str(message.from_user.id)
    ids_file = open('user_ids_db.txt', 'r')
    lines1 = ids_file.readlines()
    for line in lines1:
        if user_id in line:
            is_in_db = True
            user_id_class = line
            break
    ids_file.close()
    if is_in_db:
        user_class = class_id[user_id_class[0:3]]
        mes = 'Нашел тебя в базе данных. Твой класс: ' + user_class + '. Выбери, что делать дальше'
        menu = kb1()
        await message.answer(mes, reply_markup=menu)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        c1 = types.KeyboardButton('7А')
        c2 = types.KeyboardButton('7Б')
        c3 = types.KeyboardButton('7В')
        c4 = types.KeyboardButton('7Г')
        c5 = types.KeyboardButton('8А')
        c6 = types.KeyboardButton('8Б БМ')
        c7 = types.KeyboardButton('8Б ФХ')
        c8 = types.KeyboardButton('8В')
        c9 = types.KeyboardButton('8Г')
        c10 = types.KeyboardButton('8Д')
        c11 = types.KeyboardButton('9А ФМ')
        c12 = types.KeyboardButton('9А МИ')
        c13 = types.KeyboardButton('9Б')
        c14 = types.KeyboardButton('9В')
        c15 = types.KeyboardButton('9Г')
        c16 = types.KeyboardButton('9Д')
        c17 = types.KeyboardButton('10А ФМ')
        c18 = types.KeyboardButton('10А МЭ')
        c19 = types.KeyboardButton('10Б')
        c20 = types.KeyboardButton('10В БМ')
        c21 = types.KeyboardButton('10В ГУМ')
        c22 = types.KeyboardButton('11А')
        c23 = types.KeyboardButton('11Б')
        c24 = types.KeyboardButton('11В МИ')
        c25 = types.KeyboardButton('11В БМ')
        c26 = types.KeyboardButton('11Г')
        c27 = types.KeyboardButton('11Д')

        keyboard.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21,
                     c22, c23, c24, c25, c26, c27)
        await message.answer(
            'Похоже, что ты здесь впервые\U0001F44B Выбери класс, в котором учишься, чтобы получать актуальную '
            'информацию о заменах',
            reply_markup=keyboard)


@dp.message_handler(commands=['ZV'])
async def substitutions(message: types.Message, state: FSMContext):
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Галя, отмена!')
    btn2 = types.KeyboardButton('Новый день')
    kbrd.add(btn, btn2)
    await message.answer(
        'Ты в редакторе замен. Отправь мне в виде сообщения класс, в котором завтра будут замены. Например: 9А '
        'ФМ\nПеред тем, как начать вводить новые замены, напиши Новый день',
        reply_markup=kbrd)
    await UserState.choosing_class.set()


@dp.message_handler(
    lambda message: message.text in checker or message.text in class_stream or message.text == 'Новый день',
    state=UserState.choosing_class)
async def choosing_class(message: types.Message, state: FSMContext):
    bt = types.KeyboardButton('Подтвердить')
    bt3 = types.KeyboardButton('Галя, отмена!')
    kbr = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbr.add(bt, bt3)
    if message.text == 'Новый день':
        open('subs.txt', 'w').close()
        open('subsp.txt', 'w').close()
    elif message.text in class_stream:
        streamed = stream_id[message.text]
        async with state.proxy() as data1:
            data1['classes'] = streamed
        await message.answer(
            'Теперь вводи замены. Каждую замену отправляй отдельным сообщением.\nФормат: Время, Предмет, '
            'Вместо [Учителя] - [Учитель], Кабинет.\nПример: 9:00, история, вместо Чалковой Д. Р. - Фомин С. А., '
            '417\nВНИМАНИЕ! Поточные замены не затрагивают гуманитарные классы, их нужно вводить отдельно.\nЕсли '
            'необходимо откорректировать замены, воспользуйся командой /230 для рассылки сообщения\nПосле завершения '
            'нажмите Подтвердить.', reply_markup=kbr)
        await UserState.typing_subs_stream.set()
    else:
        id_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
        async with state.proxy() as data1:
            data1['class'] = id_class
        await message.answer(
            'Теперь вводи замены. Каждую замену отправляй отдельным сообщением.\nФормат: Время, Предмет, '
            'Вместо [Учителя] - [Учитель], Кабинет.\nПример: 9:00, история, вместо Чалковой Д. Р. - Фомин С. А., '
            '417\nВНИМАНИЕ! Если необходимо откорректировать замены, воспользуйся командой /230 для рассылки '
            'сообщения\nПосле завершения нажмите Подтвердить.',
            reply_markup=kbr)
        await UserState.typing_subs.set()


@dp.message_handler(lambda message: message.text != 'Галя, отмена!', state=UserState.typing_subs)
async def typing(message: types.Message, state: FSMContext):
    async with state.proxy() as data1:
        id_class = data1['class']
    if message.text == 'Подтвердить':
        knop = types.KeyboardButton('Галя, отмена!')
        klav = types.ReplyKeyboardMarkup(resize_keyboard=True)
        klav.add(knop)
        text_class = class_id[id_class]
        sending = []
        mes = text_class + ', замены на завтра:' + '\n'
        f = open('subs.txt', 'r')
        lines = f.readlines()
        for line in lines:
            if line[0:3] == id_class:
                sending.append(line[5::])
        for d in sending:
            mes += d + '\n'
        f.close()
        file_id = open('user_ids_db.txt', 'r')
        lines_new = file_id.readlines()
        for b in lines_new:
            if id_class in b:
                await bot.send_message(chat_id=int(b[3::]), text=mes)
        await message.answer('Замены отправлены пользователям из класса ' + text_class, reply_markup=klav)
        await UserState.choosing_class.set()
    else:
        f = open('subs.txt', 'a')
        f.write(id_class + ': ' + message.text + '\n')
        f.close()


@dp.message_handler(lambda message: message.text != 'Галя, отмена!', state=UserState.typing_subs_stream)
async def stream_subs(message: types.Message, state: FSMContext):
    async with state.proxy() as data1:
        id_classes = data1['classes']
    if message.text == 'Подтвердить':
        knop = types.KeyboardButton('Галя, отмена!')
        klav = types.ReplyKeyboardMarkup(resize_keyboard=True)
        klav.add(knop)
        sending = []
        mes = 'Замены на завтра(поток):' + '\n'
        f = open('subsp.txt', 'r')
        lines = f.readlines()
        for line in lines:
            if line[0:3] in id_classes:
                sending.append(line[5::])
        for d in sending:
            if d in mes:
                continue
            else:
                mes += d + '\n'
        f.close()
        file_id = open('user_ids_db.txt', 'r')
        lines_new = file_id.readlines()
        for id_class in id_classes:
            for b in lines_new:
                if id_class in b:
                    await bot.send_message(chat_id=int(b[3::]), text=mes)
        await message.answer('Замены отправлены пользователям из класса выбранной параллели', reply_markup=klav)
        await UserState.choosing_class.set()
    else:
        for id_class in id_classes:
            f = open('subsp.txt', 'a')
            f.write(id_class + ': ' + message.text + '\n')
            f.close()


@dp.message_handler(commands=['230'])
async def sender(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn30 = types.KeyboardButton('Галя, отмена!')
    kb.add(btn30)
    await message.answer('Введите текст для рассылки', reply_markup=kb)
    await UserState.sending.set()


@dp.message_handler(lambda message: message.text != 'Галя, отмена!', state=UserState.sending)
async def sender_two(message: types.Message, state: FSMContext):
    kb = kb1()
    sender_id = []
    f = open('user_ids_db.txt', 'r')
    lines = f.readlines()
    for line in lines:
        print(line[4:-2])
        sender_id.append(int(line[3::]))
    for ids in sender_id:
        await bot.send_message(chat_id=ids, text=message.text)
    await message.answer('Отправлено!', reply_markup=kb)
    await state.finish()


@dp.message_handler(lambda message: check(str(message.from_user.id)), lambda message: message.text in checker)
async def save_id(message: types.Message):
    user_id = str(message.from_user.id)
    id_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
    ids_file = open('user_ids_db.txt', 'a')
    id_full = id_class + user_id
    ids_file.write(id_full + '\n')
    ids_file.close()
    menu1 = kb1()
    markup = types.ReplyKeyboardMarkup(keyboard=menu1, resize_keyboard=True, row_width=1)
    await message.answer('Ты в главном меню', reply_markup=markup)


@dp.message_handler(commands=['finish'])
async def finishing(message: types.Message):
    f1 = open('user_ids_db.txt', 'r').readlines()
    f2 = open('subs.txt', 'r').read()
    f3 = open('subsp.txt', 'r').read()
    for line in f1:
        if line[0:3] not in f2 and line[0:3] not in f3:
            await bot.send_message(chat_id=int(line[3::]), text=class_id[line[0:3]] + ' - замен на завтра нет')
        else:
            continue


@dp.message_handler(lambda message: message.text == 'Изменить любимый класс\U0001F504')
async def new_class(message: types.Message):
    markup5 = kb()
    await UserState.changing_class.set()
    await message.answer('Выбери новый класс', reply_markup=markup5)


@dp.message_handler(lambda message: message.text in checker, state=UserState.changing_class)
async def class_id_changing(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    file_ids = open('user_ids_db.txt', 'r')
    lines = file_ids.readlines()
    for line in lines:
        if user_id in line:
            lines.remove(line)
            break
    file_ids.close()
    id_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
    file_ids = open('user_ids_db.txt', 'w')
    new = id_class + user_id
    lines.append(new + '\n')
    file_ids.writelines(lines)
    file_ids.close()
    new_menu = kb1()
    await state.finish()
    await message.answer('Успешно изменено. Возвращаемся в главное меню', reply_markup=new_menu)


@dp.message_handler(lambda message: message.text == 'Посмотреть замены\U0001F440')
async def view_subs(message: types.Message):
    f = open('subs.txt', 'r')
    f2 = open('user_ids_db.txt', 'r')
    f3 = open('subsp.txt', 'r')
    lines = f.readlines()
    lines2 = f2.readlines()
    lines3 = f3.readlines()
    us_id = str(message.from_user.id)
    for line2 in lines2:
        if us_id in line2:
            class_ids = line2[0:3]
            break
    class_text = class_id[class_ids]
    mes = class_text + ', замены на завтра\n'
    count = 0
    f.close()
    f2.close()
    f3.close()
    for line3 in lines3:
        if class_ids in line3:
            count += 1
            mes += line3[5::]
    for line in lines:
        if class_ids in line:
            count += 1
            mes += line[5::]
    if count == 0:
        await message.answer('Замен на завтра нет')
    else:
        await message.answer(mes)


@dp.message_handler(lambda message: message.text == 'Узнать расписание\U0001F4DA')
async def ttables(message: types.Message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
    btn7 = types.KeyboardButton('Расписание другого класса')
    btn8 = types.KeyboardButton('Вернуться в меню\U0001F3E0')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    await message.answer('Выбери день', reply_markup=markup2)


@dp.message_handler(lambda message: message.text in checking)
async def tt(message: types.Message):
    user_id = str(message.from_user.id)
    file_id = open('user_ids_db.txt', 'r')
    lines = file_id.readlines()
    for line in lines:
        if user_id in line:
            user_class_id = line[0:3]
            break
    weekday = days[message.text]
    tt = get_tt(weekday, user_class_id)
    count = 1
    mes_tt = ''
    for i in tt:
        mes_tt += str(count) + '. ' + i + '\n'
        count += 1
    mes_tt_final = message.text + ':' + '\n' + mes_tt
    await message.answer(mes_tt_final)



@dp.message_handler(lambda message: message.text == 'Фото расписания\U0001F4F8')
async def photo_tt(message: types.Message):
    user_id = str(message.from_user.id)
    file_id = open('user_ids_db.txt', 'r')
    lines2 = file_id.readlines()
    for line in lines2:
        if user_id in line:
            user_class_id = line[0:3]
            break
    id_photo = tt_photo(user_class_id)
    await message.answer_photo(id_photo)


@dp.message_handler(lambda message: message.text == 'Расписание другого класса')
async def other_tt(message: types.Message):
    kb3 = kb2()
    await UserState.other_ttable.set()
    await message.answer('Выбери класс', reply_markup=kb3)


@dp.message_handler(lambda message: message.text in checker, state=UserState.other_ttable)
async def choice(message: types.Message, state: FSMContext):
    a = list(class_id.keys())[list(class_id.values()).index(message.text)]
    async with state.proxy() as data:
        data['class_id'] = a

    markup10 = kb4()
    await UserState.other_act.set()
    await message.answer('Выбери день', reply_markup=markup10)


@dp.message_handler(lambda message: message.text in checker3, state=UserState.other_act)
async def action(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        a = data['class_id']
    if message.text in checking:
        day = message.text
        weekday = days[day]
        tt = get_tt(weekday, a)
        count = 1
        mes_tt = ''
        for i in tt:
            mes_tt += str(count) + '. ' + i + '\n'
            count += 1
        mes_tt_final = day + ':' + '\n' + mes_tt
        await message.answer(mes_tt_final)
    elif message.text == 'Фото\U0001F4F8':
        photo_id = tt_photo(a)
        await message.answer_photo(photo_id)


@dp.message_handler(lambda message: message.text == 'Вернуться в меню\U0001F3E0', state='*')
async def main_menu(message: types.Message, state: FSMContext):
    kb = kb1()
    await state.finish()
    await message.answer('Ты вернулся в главное меню', reply_markup=kb)


@dp.message_handler(lambda message: message.text == 'Назад', state=UserState.other_ttable)
async def back_my_class(message: types.Message, state: FSMContext):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
    btn7 = types.KeyboardButton('Расписание другого класса')
    btn8 = types.KeyboardButton('Вернуться в меню\U0001F3E0')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    await state.finish()
    await message.reply('Исполнено.', reply_markup=markup2)


@dp.message_handler(lambda message: message.text == 'Выбор класса', state=UserState.other_act)
async def back_class(message: types.Message):
    keybrd = kb2()
    await UserState.other_ttable.set()
    await message.reply('Выбери класс', reply_markup=keybrd)


@dp.message_handler(lambda message: message.text == 'Галя, отмена!', state='*')
async def cancel(message: types.Message, state: FSMContext):
    await message.answer('Отменено.', reply_markup=kb1())
    await state.finish()


@dp.message_handler(
    lambda message: message.text not in checker3 and message.text not in checker4, state='*')
async def other_mes(message: types.Message):
    await message.answer(
        'Скорее всего, ты ввел эту команду, потому что ошибся или захотел сломать бота. Пожалуйста, воспользуйся '
        'клавиатурой на экране')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as error:
        log = open('utils/bot_log.txt', 'a')
        log.write(str(error) + '\n')

