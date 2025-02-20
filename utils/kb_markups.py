from aiogram import types
def sub_kb():
    kbsub = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = types.KeyboardButton('Новый день')
    b2 = types.KeyboardButton('Отправить')
    b3 = types.KeyboardButton('Галя, отмена!')
    kbsub.add(b1, b2, b3)
    return kbsub


def first_time_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1 = types.KeyboardButton('6А')
    c2 = types.KeyboardButton('6Б')
    c3 = types.KeyboardButton('7А')
    c4 = types.KeyboardButton('7Б')
    c5 = types.KeyboardButton('7В')
    c6 = types.KeyboardButton('8А')
    c7 = types.KeyboardButton('8Б')
    c8 = types.KeyboardButton('8В ФМ')
    c9 = types.KeyboardButton('8В МЭ')
    c10 = types.KeyboardButton('8Г')
    c11 = types.KeyboardButton('9А')
    c12 = types.KeyboardButton('9Б ФХ')
    c13 = types.KeyboardButton('9Б БМ')
    c14 = types.KeyboardButton('9В')
    c15 = types.KeyboardButton('9Г')
    c16 = types.KeyboardButton('9Д')
    c17 = types.KeyboardButton('10А ФМ')
    c18 = types.KeyboardButton('10А БМ')
    c19 = types.KeyboardButton('10Б')
    c20 = types.KeyboardButton('10В МИ')
    c21 = types.KeyboardButton('10В ГУМ')
    c22 = types.KeyboardButton('10Г')
    c23 = types.KeyboardButton('11А ФМ')
    c24 = types.KeyboardButton('11А МЭ')
    c25 = types.KeyboardButton('11Б')
    c26 = types.KeyboardButton('11В БМ')
    c27 = types.KeyboardButton('11В ГУМ')
    keyboard.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21,
                 c22, c23, c24, c25, c26, c27)
    return keyboard

def kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1 = types.KeyboardButton('6А')
    c2 = types.KeyboardButton('6Б')
    c3 = types.KeyboardButton('7А')
    c4 = types.KeyboardButton('7Б')
    c5 = types.KeyboardButton('7В')
    c6 = types.KeyboardButton('8А')
    c7 = types.KeyboardButton('8Б')
    c8 = types.KeyboardButton('8В ФМ')
    c9 = types.KeyboardButton('8В МЭ')
    c10 = types.KeyboardButton('8Г')
    c11 = types.KeyboardButton('9А')
    c12 = types.KeyboardButton('9Б ФХ')
    c13 = types.KeyboardButton('9Б БМ')
    c14 = types.KeyboardButton('9В')
    c15 = types.KeyboardButton('9Г')
    c16 = types.KeyboardButton('9Д')
    c17 = types.KeyboardButton('10А ФМ')
    c18 = types.KeyboardButton('10А БМ')
    c19 = types.KeyboardButton('10Б')
    c20 = types.KeyboardButton('10В МИ')
    c21 = types.KeyboardButton('10В ГУМ')
    c22 = types.KeyboardButton('10Г')
    c23 = types.KeyboardButton('11А ФМ')
    c24 = types.KeyboardButton('11А МЭ')
    c25 = types.KeyboardButton('11Б')
    c26 = types.KeyboardButton('11В БМ')
    c27 = types.KeyboardButton('11В ГУМ')
    c28 = types.KeyboardButton('Домой\U0001F3E0')
    keyboard.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22,
                 c23, c24, c25, c26, c27, c28)
    return keyboard


def kb2():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1 = types.KeyboardButton('6А')
    c2 = types.KeyboardButton('6Б')
    c3 = types.KeyboardButton('7А')
    c4 = types.KeyboardButton('7Б')
    c5 = types.KeyboardButton('7В')
    c6 = types.KeyboardButton('8А')
    c7 = types.KeyboardButton('8Б')
    c8 = types.KeyboardButton('8В ФМ')
    c9 = types.KeyboardButton('8В МЭ')
    c10 = types.KeyboardButton('8Г')
    c11 = types.KeyboardButton('9А')
    c12 = types.KeyboardButton('9Б ФХ')
    c13 = types.KeyboardButton('9Б БМ')
    c14 = types.KeyboardButton('9В')
    c15 = types.KeyboardButton('9Г')
    c16 = types.KeyboardButton('9Д')
    c17 = types.KeyboardButton('10А ФМ')
    c18 = types.KeyboardButton('10А БМ')
    c19 = types.KeyboardButton('10Б')
    c20 = types.KeyboardButton('10В МИ')
    c21 = types.KeyboardButton('10В ГУМ')
    c22 = types.KeyboardButton('10Г')
    c23 = types.KeyboardButton('11А ФМ')
    c24 = types.KeyboardButton('11А МЭ')
    c25 = types.KeyboardButton('11Б')
    c26 = types.KeyboardButton('11В БМ')
    c27 = types.KeyboardButton('11В ГУМ')
    c28 = types.KeyboardButton('Назад')
    keyboard.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22,
                 c23, c24, c25, c26, c27, c28)
    return keyboard


def call_kb():
    calling = types.InlineKeyboardMarkup(row_width=2)
    call0 = types.InlineKeyboardButton(text='Да✅', callback_data='yes')
    call1 = types.InlineKeyboardButton(text='Нет❌', callback_data='no')
    calling.add(call0, call1)
    return calling


def call_settings():
    kb = types.InlineKeyboardMarkup(row_width=1)
    call1 = types.InlineKeyboardButton(text='Выбрать формат расписания✅', callback_data='format')
    call2 = types.InlineKeyboardButton(text='Изменить роль\U0001F504', callback_data='1change role')
    call3 = types.InlineKeyboardButton(text='Выход❌', callback_data='menu')
    kb.add(call1, call2, call3)
    return kb


def call_classes():
    kb = types.InlineKeyboardMarkup(row_width=1)
    c0 = types.InlineKeyboardButton(text='6-е классы', callback_data='t6')
    c1 = types.InlineKeyboardButton(text='7-е классы', callback_data='t7')
    c2 = types.InlineKeyboardButton(text='8-е классы', callback_data='t8')
    c3 = types.InlineKeyboardButton(text='9-е классы', callback_data='t9')
    c4 = types.InlineKeyboardButton(text='10-е классы', callback_data='t10')
    c5 = types.InlineKeyboardButton(text='11-е классы', callback_data='t11')
    c6 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    kb.add(c0, c1, c2, c3, c4, c5, c6)
    return kb


def call_six():
    kb6 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='6А', callback_data='c01')
    c2 = types.InlineKeyboardButton(text='6Б', callback_data='c02')
    c3 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb6.add(c1, c2, c3)
    return kb6


def call_seven():
    kb7 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='7А', callback_data='c03')
    c2 = types.InlineKeyboardButton(text='7Б', callback_data='c04')
    c3 = types.InlineKeyboardButton(text='7В', callback_data='c05')
    c4 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb7.add(c1, c2, c3, c4)
    return kb7


def call_eight():
    kb8 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='8А', callback_data='c06')
    c2 = types.InlineKeyboardButton(text='8Б', callback_data='c07')
    c3 = types.InlineKeyboardButton(text='8В ФМ', callback_data='c08')
    c4 = types.InlineKeyboardButton(text='8В МЭ', callback_data='c09')
    c5 = types.InlineKeyboardButton(text='8Г', callback_data='c10')
    c6 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb8.add(c1, c2, c3, c4, c5, c6)
    return kb8


def call_nine():
    kb9 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='9А', callback_data='c11')
    c2 = types.InlineKeyboardButton(text='9Б ФХ', callback_data='c12')
    c3 = types.InlineKeyboardButton(text='9Б БМ', callback_data='c13')
    c4 = types.InlineKeyboardButton(text='9В', callback_data='c14')
    c5 = types.InlineKeyboardButton(text='9Г', callback_data='c15')
    c6 = types.InlineKeyboardButton(text='9Д', callback_data='c16')
    c7 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb9.add(c1, c2, c3, c4, c5, c6, c7)
    return kb9


def call_ten():
    kb10 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='10А ФМ', callback_data='c17')
    c2 = types.InlineKeyboardButton(text='10А БМ', callback_data='c18')
    c3 = types.InlineKeyboardButton(text='10Б', callback_data='c19')
    c4 = types.InlineKeyboardButton(text='10В МИ', callback_data='c20')
    c5 = types.InlineKeyboardButton(text='10В ГУМ', callback_data='c21')
    c6 = types.InlineKeyboardButton(text='10Г', callback_data='c22')
    c7 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb10.add(c1, c2, c3, c4, c5, c6, c7)
    return kb10


def call_eleven():
    kb11 = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text='11А ФМ', callback_data='c23')
    c2 = types.InlineKeyboardButton(text='11А МЭ', callback_data='c24')
    c3 = types.InlineKeyboardButton(text='11Б', callback_data='c25')
    c4 = types.InlineKeyboardButton(text='11В БМ', callback_data='c26')
    c5 = types.InlineKeyboardButton(text='11В ГУМ', callback_data='c27')
    c6 = types.InlineKeyboardButton(text='\U0001F519Назад', callback_data='1class_back')
    kb11.add(c1, c2, c3, c4, c5, c6)
    return kb11


def kb1():
    kbrd = [
        [types.KeyboardButton('Узнать расписание\U0001F4DA')],
        [types.KeyboardButton('Изменить любимый класс\U0001F504')],
        [types.KeyboardButton('Посмотреть замены\U0001F440')],
        [types.KeyboardButton('Меню\U0001F372')]
    ]
    markup4 = types.ReplyKeyboardMarkup(keyboard=kbrd, resize_keyboard=True, row_width=1)
    return markup4


def kb1_photo():
    kb_main = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    m1 = types.KeyboardButton('Узнать расписание\U0001F4DA')
    m2 = types.KeyboardButton('Расписание другого класса\U0001F4D5')
    m3 = types.KeyboardButton('Изменить любимый класс\U0001F504')
    m4 = types.KeyboardButton('Посмотреть замены\U0001F440')
    m5 = types.KeyboardButton('Меню\U0001F372')
    kb_main.add(m1, m2, m3, m4, m5)
    return kb_main


def kb4():
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn0 = types.KeyboardButton('Назад')
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото\U0001F4F8')
    btn8 = types.KeyboardButton('Выбор класса')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8, btn0)
    return markup2


def teachers_main():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn0 = types.KeyboardButton('Моё расписание\U0001F4DA')
    btn1 = types.KeyboardButton('Расписание учеников\U0001F4D5')
    btn2 = types.KeyboardButton('Выбрать другого учителя\U0001F504')
    btn3 = types.KeyboardButton('Замены учеников\U0001F440')
    btn4 = types.KeyboardButton('Меню\U0001F372')
    menu.add(btn0, btn1, btn2, btn3, btn4)
    return menu


def teacher_text_tt():
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото расписания\U0001F4F8')
    btn8 = types.KeyboardButton('Домой\U0001F3E0')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8)
    return markup2


def menu_days():
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Домой\U0001F3E0')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup2


def teacher_action():
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn0 = types.KeyboardButton('Домой\U0001F3E0')
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Фото\U0001F4F8')
    btn8 = types.KeyboardButton('Выбор класса')
    markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8, btn0)
    return markup2
