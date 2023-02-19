from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from data_operating import *
from utils.kb_markups import *
from local_vars import *
import datetime
from config import PROXY_URL, API_TOKEN

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    choosing_class = State()
    typing_subs = State()
    sending = State()
    typing_subs_stream = State()
    other_ttable = State()
    other_act = State()
    changing_class = State()
    subclass = State()
    watch_student = State()
    action_teacher = State()
    choosing_another_teacher = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    not_in_db = check(str(message.from_user.id))
    if not not_in_db:
        full_info = get_information(str(message.from_user.id))
        if full_info[3] == 'student':
            mes = f'Нашел тебя в базе данных. Твой класс: {class_id[full_info[0]]}. Выбери, что делать дальше'
            await message.answer(mes, reply_markup=kb1())
        elif full_info[3] == 'teacher':
            sfl = teachers_id[full_info[0]].split(' ')
            await message.answer(f'Добро пожаловать, {sfl[1]} {sfl[2]}', reply_markup=teachers_main())
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton('Я учитель\U0001F9D1')
        b2 = types.KeyboardButton('Я ученик\U0001F9D1')
        kb.add(b1, b2)
        await message.answer(
            'Здравствуйте\U0001F44B\nКто вы: учитель или ученик?', reply_markup=kb)


@dp.message_handler(lambda message: message.text == 'Я учитель\U0001F9D1' or message.text == 'Я ученик\U0001F9D1')
async def first_time_role(message: types.Message):
    if message.text == 'Я учитель\U0001F9D1':
        await message.answer('Принято. Для завершения регистрации отправьте Вашу фамилию и имя.\nНапример: <b>Ларионов Сергей</b>', parse_mode='HTML')
    elif message.text == 'Я ученик\U0001F9D1':
        await message.answer('Отлично! Выбери класс, в котором учишься, чтобы получать актуальную информацию о заменах', reply_markup=first_time_kb())


@dp.message_handler(lambda message: check(str(message.from_user.id)), lambda message: message.text in checker)
async def save_id(message: types.Message):
    user_id = str(message.from_user.id)
    id_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
    with open('user_ids_db.txt', 'a') as ids_file:
        id_full = id_class + user_id
        ids_file.write(id_full + '\n')
    save_information(id_class, user_id, 'student')
    await message.answer('Ты в главном меню', reply_markup=kb1())


@dp.message_handler(lambda message: check(str(message.from_user.id)), lambda message: message.text in list(t_enter.keys()))
async def save_tid(message: types.Message):
    t_id = t_enter[message.text]
    user_id = str(message.from_user.id)
    sfl = teachers_id[t_id].split(' ')
    with open('user_ids_db.txt', 'a') as ids_file:
        id_full = t_id + user_id
        ids_file.write(id_full + '\n')
    save_information(t_id, user_id, 'teacher')
    await message.answer(f'Добро пожаловать, {sfl[1]} {sfl[2]}!', reply_markup=teachers_main())


@dp.message_handler(commands=['settings'])
async def setting_cb(message: types.Message):
    await message.answer('В настройках Вы можете изменить роль или выбрать удобный для Вас формат расписания', reply_markup=call_settings())


@dp.callback_query_handler(text='format')
async def format_changing(call: types.CallbackQuery, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(call.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    kb = types.InlineKeyboardMarkup(row_width=1)
    c2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    if info[2] == 'text':
        c1 = types.InlineKeyboardButton(text='Выбрать формат: фото', callback_data='1change to photo')
        kb.add(c1, c2)
        await call.message.edit_text('Подтвердите изменение формата расписания. Текущий формат: текст', reply_markup=kb)
    elif info[2] == 'photo':
        c1 = types.InlineKeyboardButton(text='Выбрать формат: текст', callback_data='1change to text')
        kb.add(c1, c2)
        await call.message.edit_text('Подтвердите изменение формата расписания. Текущий формат: фото', reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text='1change to photo')
async def change_to_photo(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        info = data['information']
    update_format(str(call.from_user.id), 'photo')
    if info[3] == 'teacher':
        await call.message.answer('Выбран формат: фото', reply_markup=teachers_main())
    elif info[3] == 'student':
        await call.message.answer('Выбран формат: фото', reply_markup=kb1_photo())
    await state.reset_data()
    await call.message.edit_text('Формат расписания успешно изменен', reply_markup=call_settings())
    await call.answer()


@dp.callback_query_handler(text='1change to text')
async def change_to_photo(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        info = data['information']
    update_format(str(call.from_user.id), 'text')
    if info[3] == 'teacher':
        await call.message.answer('Выбран формат: текст', reply_markup=teachers_main())
    elif info[3] == 'student':
        await call.message.answer('Выбран формат: текст', reply_markup=kb1())
    await state.reset_data()
    await call.message.edit_text('Формат расписания успешно изменен', reply_markup=call_settings())
    await call.answer()


@dp.callback_query_handler(text='1change role')
async def change_role(call: types.CallbackQuery, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(call.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    kb = types.InlineKeyboardMarkup(row_width=1)
    c2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    if info[3] == 'student':
        c1 = types.InlineKeyboardButton(text='Выбрать роль: учитель', callback_data='1change to teacher')
        kb.add(c1, c2)
        await call.message.edit_text('Подтвердите изменение роли. Текущая роль: ученик', reply_markup=kb)
    elif info[3] == 'teacher':
        c1 = types.InlineKeyboardButton(text='Выбрать роль: ученик', callback_data='1change to student')
        kb.add(c1, c2)
        await call.message.edit_text('Подтвердите изменение роли. Текущая роль: учитель', reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text='1change to teacher')
async def change_to_teacher(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Для завершения отправьте фамилию и имя учителя.\nНапример: <b>Иньков Владислав</b>', parse_mode='HTML')
    await call.answer()


@dp.message_handler(lambda message: not check(str(message.from_user.id)), lambda message: message.text in list(t_enter.keys()))
async def teacher_choice(message: types.Message, state: FSMContext):
    t_id = t_enter[message.text]
    sfl = teachers_id[t_id].split(' ')
    update_role(str(message.from_user.id), t_id, 'teacher')
    await state.reset_data()
    await message.answer('Успешно изменено', reply_markup=call_settings())
    await message.answer(f'Добро пожаловать, {sfl[1]} {sfl[2]}', reply_markup=teachers_main())


@dp.callback_query_handler(text='1change to student')
async def change_to_student(call: types.CallbackQuery):
    await call.message.edit_text('Выберите класс из списка ниже', reply_markup=call_classes())
    await call.answer()


@dp.callback_query_handler(Text(startswith='t'))
async def class_choice(call: types.CallbackQuery):
    p = call.data[1::]
    if p == '7':
        await call.message.edit_text('Седьмые классы:', reply_markup=call_seven())
    elif p == '8':
        await call.message.edit_text('Восьмые классы:', reply_markup=call_eight())
    elif p == '9':
        await call.message.edit_text('Девятые классы:', reply_markup=call_nine())
    elif p == '10':
        await call.message.edit_text('Десятые классы:', reply_markup=call_ten())
    elif p == '11':
        await call.message.edit_text('Одиннадцатые классы:', reply_markup=call_eleven())
    await call.answer()


@dp.callback_query_handler(Text(startswith='c'))
async def finish_class(call: types.CallbackQuery, state: FSMContext):
    info = get_information(str(call.from_user.id))
    id_class = call.data
    update_role(str(call.from_user.id), id_class, 'student')
    await state.reset_data()
    await call.message.edit_text('Успешно изменено', reply_markup=call_settings())

    if info[2] == 'photo':
        await call.message.answer(f'Выбран класс: {class_id[id_class]}', reply_markup=kb1_photo())
    elif info[2] == 'text':
        await call.message.answer(f'Выбран класс: {class_id[id_class]}', reply_markup=kb1())
    await call.answer()


@dp.callback_query_handler(text='1class_back')
async def back_class(call: types.CallbackQuery):
    await call.message.edit_text('Выберите класс из списка ниже', reply_markup=call_classes())
    await call.answer()


@dp.callback_query_handler(text='back')
async def back_to_menu(call: types.CallbackQuery):
    await call.message.edit_text('Настройки:', reply_markup=call_settings())
    await call.answer()


@dp.callback_query_handler(text='menu')
async def quit_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer()


@dp.message_handler(commands=['update'])
async def updating(message: types.Message):
    with open('user_ids_db.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            info = get_information(line[3:-1])
            try:
                if info[3] == 'teacher':
                    await bot.send_message(chat_id=int(line[3::]), text='Бот запущен', reply_markup=teachers_main())
                elif info[3] == 'student':
                    if info[2] == 'text':
                        await bot.send_message(chat_id=int(line[3::]), text='Бот запущен', reply_markup=kb1())
                    elif info[2] == 'photo':
                        await bot.send_message(chat_id=int(line[3::]), text='Бот запущен', reply_markup=kb1_photo())
            except Exception:
                continue
    await message.answer('Done')


@dp.message_handler(commands=['ZV'])
async def substitutions(message: types.Message, state: FSMContext):
    await message.answer(
        'Ты в редакторе замен. Отправь мне в виде сообщения класс, в котором завтра будут замены. Например: 9А '
        'ФМ\nПеред тем, как начать вводить новые замены, напиши Новый день',
        reply_markup=sub_kb())
    await UserState.choosing_class.set()


@dp.message_handler(
    lambda message: message.text in checker or message.text in class_stream or message.text == 'Новый день' or message.text == 'Отправить',
    state=UserState.choosing_class)
async def choosing_class(message: types.Message, state: FSMContext):
    bt3 = types.KeyboardButton('К выбору класса')
    kbr = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbr.add(bt3)
    if message.text == 'Отправить':
        subs = {}
        classes = []
        f = open('subs.txt', 'r')
        lines = f.readlines()
        del(lines[0])
        for line in lines:
            if line[0:3] not in classes:
                classes.append(line[0:3])
        for classing in classes:
            sub = ''
            for line in lines:
                if classing in line and line[5::] not in sub:
                    sub += line[5::]
            subs[classing] = sub
        f.close()
        with open('user_ids_db.txt', 'r') as file_id:
            users = file_id.readlines()
            class_ids = list(subs.keys())
            for c in class_ids:
                sending = []
                mes = f'{class_id[c]}, замены на завтра:\n' + subs[c]
                for u in users:
                    if c in u:
                        sending.append(u[3::])
                for s in sending:
                    try:
                        await bot.send_message(chat_id=int(s), text=mes)
                    except Exception:
                        continue
        await message.answer('Замены отправлены пользователям')
    elif message.text == 'Новый день':
        open('subs.txt', 'w').close()
        with open('subs.txt', 'w') as dating:
            day_int = datetime.date.today().weekday() + 1
            if day_int == 7:
                day_int = 0
            dating.write(str(day_int) + '\n')
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


@dp.message_handler(lambda message: message.text != 'К выбору класса', state=UserState.typing_subs)
async def typing(message: types.Message, state: FSMContext):
    async with state.proxy() as data1:
        id_class = data1['class']
    with open('subs.txt', 'a') as f:
        f.write(id_class + ': ' + message.text + '\n')


@dp.message_handler(lambda message: message.text != 'К выбору класса', state=UserState.typing_subs_stream)
async def stream_subs(message: types.Message, state: FSMContext):
    async with state.proxy() as data1:
        id_classes = data1['classes']
    with open('subs.txt', 'a') as f:
        for id_class in id_classes:
            f.write(id_class + ': ' + message.text + '\n')


@dp.message_handler(lambda message: message.text == 'К выбору класса', state='*')
async def back_again(message: types.Message, state: FSMContext):
    await UserState.choosing_class.set()
    await message.answer('Отправьте класс', reply_markup=sub_kb())


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
        sender_id.append(int(line[3::]))
    for ids in sender_id:
        try:
            await bot.send_message(chat_id=ids, text=message.text)
        except Exception:
            continue
    await message.answer('Отправлено!', reply_markup=kb)
    await state.finish()


@dp.message_handler(commands=['finish'])
async def finishing(message: types.Message):
    f1 = open('user_ids_db.txt', 'r').readlines()
    f2 = open('subs.txt', 'r').read()
    for line in f1:
        if line[0:3] not in f2:
            try:
                await bot.send_message(chat_id=int(line[3::]), text=f'{class_id[line[0:3]]} - замен на завтра нет')
            except Exception:
                continue
        else:
            continue


@dp.message_handler(lambda message: message.text == 'Изменить любимый класс\U0001F504')
async def new_class(message: types.Message):
    markup5 = kb()
    await UserState.changing_class.set()
    await message.answer('Выбери новый класс', reply_markup=markup5)


@dp.message_handler(lambda message: message.text in checker, state=UserState.changing_class)
async def class_id_changing(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    with open('user_ids_db.txt', 'r') as file_ids:
        lines = file_ids.readlines()
        for line in lines:
            if info[1] in line:
                lines.remove(line)
                break
    id_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
    with open('user_ids_db.txt', 'w') as file_ids:
        new = id_class + info[1]
        lines.append(new + '\n')
        file_ids.writelines(lines)
    update_class(id_class, info[1])
    await state.reset_state()
    if info[2] == 'text':
        await message.answer('Успешно изменено. Возвращаемся в главное меню', reply_markup=kb1())
    elif info[2] == 'photo':
        await message.answer('Успешно изменено. Возвращаемся в главное меню', reply_markup=kb1_photo())


@dp.message_handler(lambda message: message.text == 'Посмотреть замены\U0001F440')
async def view_subs(message: types.Message):
    f = open('subs.txt', 'r')
    f2 = open('user_ids_db.txt', 'r')
    lines = f.readlines()
    lines2 = f2.readlines()
    us_id = str(message.from_user.id)
    try:
        current = lines[0]
        day_txt = weekdays[int(current)]
        del(lines[0])
    except IndexError:
        day_txt = 'завтра'
    for line2 in lines2:
        if us_id in line2:
            class_ids = line2[0:3]
            break
    class_text = class_id[class_ids]
    mes = f'{class_text}, замены на {day_txt}:\n'
    count = 0
    f.close()
    f2.close()
    for line in lines:
        if class_ids in line:
            count += 1
            mes += line[5::]
    if count == 0:
        await message.answer('Замен на завтра нет')
        await message.answer('Хотите посмотреть замены других классов?', reply_markup=call_kb())
    else:
        await message.answer(mes)
        await message.answer('Хотите посмотреть замены других классов?', reply_markup=call_kb())


@dp.callback_query_handler(text='yes')
async def sub_agree(call: types.CallbackQuery):
    await call.message.delete()
    await UserState.subclass.set()
    await call.message.answer('Выбери класс', reply_markup=kb())
    await call.answer()


@dp.callback_query_handler(text='no')
async def sub_disagree(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.answer()


@dp.message_handler(lambda message: message.text in checker, state=UserState.subclass)
async def sub_sender(message: types.Message, state: FSMContext):
    id_of_class = list(class_id.keys())[list(class_id.values()).index(message.text)]
    with open('subs.txt', 'r') as f:
        lines = f.readlines()
    try:
        current = lines[0]
        day_txt = weekdays[int(current)]
        del(lines[0])
    except IndexError:
        day_txt = 'завтра'
    mes = f'{message.text}, замены на {day_txt}:\n'
    count = 0
    for line in lines:
        if id_of_class in line:
            count += 1
            mes += line[5::]
    if count == 0:
        await message.answer('Замен на завтра нет')
    else:
        await message.answer(mes)


@dp.message_handler(lambda message: message.text == 'Моё расписание\U0001F4DA')
async def teacher_tt(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    if info[2] == 'photo':
        id_photo = tt_photo(info[0])
        await message.answer_photo(id_photo)
    elif info[2] == 'text':
        await message.answer('Выберите день', reply_markup=teacher_text_tt())


@dp.message_handler(lambda message: message.text == 'Расписание учеников\U0001F4D5')
async def watch_student_tt(message: types.Message):
    await UserState.watch_student.set()
    await message.answer('Выберите класс, расписание которого Вы хотели бы узнать', reply_markup=kb())


@dp.message_handler(lambda message: message.text in checker, state=UserState.watch_student)
async def student_tt(message: types.Message, state: FSMContext):
    a = list(class_id.keys())[list(class_id.values()).index(message.text)]
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    if info[2] == 'photo':
        id_photo = tt_photo(a)
        await message.answer_photo(id_photo)
    elif info[2] == 'text':
        async with state.proxy() as data:
            data['class_id'] = a
        await UserState.action_teacher.set()
        await message.answer(f'Выбран класс: {message.text}', reply_markup=teacher_action())


@dp.message_handler(lambda message: message.text in checker3, state=UserState.action_teacher)
async def t_act(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        a = data['class_id']
    if message.text in checking:
        weekday = days[message.text]
        tt = get_tt(weekday, a)
        count = 1
        mes_tt = ''
        for i in tt:
            mes_tt += str(count) + '. ' + i + '\n'
            count += 1
        mes_tt_final = message.text + ':' + '\n' + mes_tt
        await message.answer(mes_tt_final)
    elif message.text == 'Фото\U0001F4F8':
        id_photo = tt_photo(a)
        await message.answer_photo(id_photo)


@dp.message_handler(lambda message: message.text == 'Выбрать другого учителя\U0001F504')
async def change_teacher(message: types.Message):
    kb_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1 = types.KeyboardButton('Отмена')
    kb_back.add(c1)
    await UserState.choosing_another_teacher.set()
    await message.answer('Для изменения отправьте фамилию и имя учителя\nНапример: <b>Заикин Евгений</b>', parse_mode='HTML', reply_markup=kb_back)


@dp.message_handler(lambda message: message.text in list(t_enter.keys()), state=UserState.choosing_another_teacher)
async def change_final(message: types.Message, state: FSMContext):
    t_id = t_enter[message.text]
    sfl = teachers_id[t_id].split(' ')
    with open('user_ids_db.txt', 'r') as file_ids:
        lines = file_ids.readlines()
    for line in lines:
        if str(message.from_user.id) in line:
            lines.remove(line)
            break
    with open('user_ids_db.txt', 'w') as file_ids:
        new = t_id + str(message.from_user.id)
        lines.append(new + '\n')
        file_ids.writelines(lines)
    update_teacher(t_id, str(message.from_user.id))
    await state.reset_state()
    await message.answer(f'Информация обновлена. Добро пожаловать, {sfl[1]} {sfl[2]}!', reply_markup=teachers_main())


@dp.message_handler(lambda message: message.text == 'Отмена', state=UserState.choosing_another_teacher)
async def cancel(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await message.answer('Вы в главном меню', reply_markup=teachers_main())


@dp.message_handler(lambda message: message.text == 'Замены учеников\U0001F440')
async def teacher_subclass(message: types.Message):
    await UserState.subclass.set()
    await message.answer('Выберите класс, замены которого Вы хотите посмотреть', reply_markup=kb())


@dp.message_handler(lambda message: message.text == 'Узнать расписание\U0001F4DA')
async def timetables(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    if info[2] == 'photo':
        id_photo = tt_photo(info[0])
        await message.answer_photo(id_photo)
    elif info[2] == 'text':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
        btn7 = types.KeyboardButton('Расписание другого класса')
        btn8 = types.KeyboardButton('Домой\U0001F3E0')
        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        await message.answer('Выбери день', reply_markup=markup2)


@dp.message_handler(lambda message: message.text in checking)
async def tt(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    weekday = days[message.text]
    tt = get_tt(weekday, info[0])
    count = 1
    mes_tt = ''
    for i in tt:
        mes_tt += str(count) + '. ' + i + '\n'
        count += 1
    mes_tt_final = message.text + ':' + '\n' + mes_tt
    await message.answer(mes_tt_final)


@dp.message_handler(lambda message: message.text == 'Фото расписания\U0001F4F8')
async def photo_tt(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    id_photo = tt_photo(info[0])
    await message.answer_photo(id_photo)


@dp.message_handler(lambda message: message.text == 'Расписание другого класса')
async def other_tt(message: types.Message):
    kb3 = kb2()
    await UserState.other_ttable.set()
    await message.answer('Выбери класс', reply_markup=kb3)


@dp.message_handler(lambda message: message.text in checker, state=UserState.other_ttable)
async def choice(message: types.Message, state: FSMContext):
    a = list(class_id.keys())[list(class_id.values()).index(message.text)]
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    if info[2] == 'photo':
        id_photo = tt_photo(a)
        await message.answer_photo(id_photo)
    elif info[2] == 'text':
        async with state.proxy() as data:
            data['class_id'] = a
        markup10 = kb4()
        await UserState.other_act.set()
        await message.answer('Выбери действие', reply_markup=markup10)


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


@dp.message_handler(lambda message: message.text == 'Домой\U0001F3E0', state='*')
async def main_menu(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    await state.reset_state(with_data=False)
    if info[3] == 'teacher':
        await message.answer('Вы вернулись в главное меню', reply_markup=teachers_main())
    elif info[3] == 'student':
        if info[2] == 'text':
            await message.answer('Ты вернулся в главное меню', reply_markup=kb1())
        elif info[2] == 'photo':
            await message.answer('Ты вернулся в главное меню', reply_markup=kb1_photo())


@dp.message_handler(lambda message: message.text == 'Назад', state=UserState.other_ttable)
async def back_my_class(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            info = data['information']
    except Exception:
        info = get_information(str(message.from_user.id))
        async with state.proxy() as data:
            data['information'] = info
    if info[2] == 'text':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
        btn7 = types.KeyboardButton('Расписание другого класса')
        btn8 = types.KeyboardButton('Домой\U0001F3E0')
        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        await state.reset_state(with_data=False)
        await message.reply('Исполнено.', reply_markup=markup2)
    elif info[2] == 'photo':
        await state.reset_state(with_data=False)
        await message.answer('Ты в главном меню', reply_markup=kb1_photo())


@dp.message_handler(lambda message: message.text == 'Назад', state=UserState.other_act)
async def back_my_class(message: types.Message, state: FSMContext):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
    btn7 = types.KeyboardButton('Расписание другого класса')
    btn8 = types.KeyboardButton('Домой\U0001F3E0')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    await state.reset_state(with_data=False)
    await message.reply('Исполнено.', reply_markup=markup2)


@dp.message_handler(lambda message: message.text == 'Выбор класса', state=UserState.other_act)
async def back_class(message: types.Message):
    keybrd = kb2()
    await UserState.other_ttable.set()
    await message.reply('Выбери класс', reply_markup=keybrd)


@dp.message_handler(lambda message: message.text == 'Выбор класса', state=UserState.action_teacher)
async def back_teacher(message: types.Message):
    await UserState.watch_student.set()
    await message.reply('Выберите класс', reply_markup=kb())


@dp.message_handler(lambda message: message.text == 'Галя, отмена!', state='*')
async def cancel(message: types.Message, state: FSMContext):
    await message.answer('Отменено.', reply_markup=kb1())
    await state.reset_state(with_data=False)


@dp.message_handler(
    lambda message: message.text not in checker3 and message.text not in checker4, state='*')
async def other_mes(message: types.Message):
    await message.answer(
        'Скорее всего, ты ввел эту команду, потому что ошибся или захотел сломать бота. Пожалуйста, воспользуйся '
        'клавиатурой на экране')


if __name__ == '__main__':
    try:
        executor.start_polling(dp, timeout=60, skip_updates=True)
    except Exception as error:
        log = open('utils/bot_log.txt', 'a')
        log.write(str(error) + '\n')

