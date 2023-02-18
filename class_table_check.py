import sqlite3
from aiogram import types
connection = sqlite3.connect('utils/ttable.db')
cur = connection.cursor()
photo_ids = {'c01': 'AgACAgIAAxkBAAIFRWO8VUPOUOVdgdwQzwc4LYQG8voxAAKYxTEbImjpSTLe0VHAZnWcAQADAgADcwADLQQ', 'c02': 'AgACAgIAAxkBAAIFR2O8VUigA8Ye98Ip57m1ne24HZWlAAKcxTEbImjpSZswEevHSc8AAQEAAwIAA3MAAy0E', 'c03': 'AgACAgIAAxkBAAIFSWO8VUw5g3EBWoYvDZ646w8XFgF3AAKdxTEbImjpSVtbuGg_hxdDAQADAgADcwADLQQ', 'c04': 'AgACAgIAAxkBAAIFS2O8VVT65ZG04fxNMTMLmlHoIr9FAAKexTEbImjpSf8gQ-39SbyjAQADAgADcwADLQQ', 'c05': 'AgACAgIAAxkBAAIFTWO8VVu2qeriYTEfXdM6jKz-nPmQAAKfxTEbImjpSV_Ddtl7J_20AQADAgADcwADLQQ', 'c06': 'AgACAgIAAxkBAAIFT2O8VWi3ESfFu1-2VeudJzDXUsDNAAKgxTEbImjpSQNBNJ2CChJQAQADAgADcwADLQQ', 'c07': 'AgACAgIAAxkBAAIFUWO8VW56M5tVZgJCpWQU6PXGtR8VAAKixTEbImjpSdUOnVgYAbRLAQADAgADcwADLQQ', 'c08': 'AgACAgIAAxkBAAIFU2O8VXI0tptHTGMn5ly3JCye1H9BAAKjxTEbImjpSX15xKLOxOmTAQADAgADcwADLQQ', 'c09': 'AgACAgIAAxkBAAIFVWO8VXYknfs1Mts1t20rjBKUTGTnAAKkxTEbImjpSVr4Dspk51rLAQADAgADcwADLQQ', 'c10': 'AgACAgIAAxkBAAIFV2O8VX7dD2ywIiXj7zElZzxhVqaNAAKlxTEbImjpSTpDcfsXwsniAQADAgADcwADLQQ', 'c11': 'AgACAgIAAxkBAAIFWWO8VYV68WYe1zChW39httgzn_uxAAKnxTEbImjpSdwAASr_cyCMSAEAAwIAA3MAAy0E', 'c12': 'AgACAgIAAxkBAAIFW2O8VY14VPpRGwzF1PB5YZF7X9kuAAKmxTEbImjpSdSSnHhNhNejAQADAgADcwADLQQ', 'c13': 'AgACAgIAAxkBAAIFXWO8VZOvwiqM4Jj23FxwjPgbI194AAKoxTEbImjpSfaX3xwd4SENAQADAgADcwADLQQ', 'c14': 'AgACAgIAAxkBAAIFX2O8VZdxKtkBJ70x_e7mZPDVEAn7AAKpxTEbImjpSZbJAAGE3hSm8QEAAwIAA3MAAy0E', 'c15': 'AgACAgIAAxkBAAIFYWO8VZwmmV-dHi5l737p0uUl6kyfAAKqxTEbImjpSVhwa-27oEqNAQADAgADcwADLQQ', 'c16': 'AgACAgIAAxkBAAIFY2O8VaEN0NeWZVqFUP5AhtVaF8IJAAKrxTEbImjpSdvKrGU7BC1KAQADAgADcwADLQQ', 'c17': 'AgACAgIAAxkBAAIFZWO8VanhoRvV7KiGO7Kk0IhccG8lAAKsxTEbImjpSYYphkx01ZVUAQADAgADcwADLQQ', 'c18': 'AgACAgIAAxkBAAIFZ2O8Va2sdzXJPSxutmRrqHclMHOEAAKtxTEbImjpSQv5x5b3yNc5AQADAgADcwADLQQ', 'c19': 'AgACAgIAAxkBAAIFaWO8VbOh5lO3IZ6QwY9msPe3UwwEAAKuxTEbImjpSbG0ZEpYQIMeAQADAgADcwADLQQ', 'c20': 'AgACAgIAAxkBAAIFa2O8VcMrzEZFC0rpw9VLyuxoDQABFQACr8UxGyJo6UlwzWBlzNQSgAEAAwIAA3MAAy0E', 'c21': 'AgACAgIAAxkBAAIFbWO8VclF9JxviYkhbIZMDtfIm1jAAAKwxTEbImjpSXyfWxLHDo_9AQADAgADcwADLQQ', 'c22': 'AgACAgIAAxkBAAIFb2O8Vc2VbE_h5nucPp0AAeBnVh1IJQACscUxGyJo6UnWUlk9jciYYgEAAwIAA3MAAy0E', 'c23': 'AgACAgIAAxkBAAIFcWO8VdTzKCh6mbx_TSuJy0rZlNNsAAKyxTEbImjpSWEBdTVitwmCAQADAgADcwADLQQ', 'c24': 'AgACAgIAAxkBAAIFc2O8VdyEw6XWa2qJD88r3n8xaw0UAAKzxTEbImjpSVqsQHSXXNh0AQADAgADcwADLQQ', 'c25': 'AgACAgIAAxkBAAIFdWO8VeB9OSQ7i7eztZ4eRgABX6GqdgACtMUxGyJo6Uk52jhahcBJmgEAAwIAA3MAAy0E', 'c26': 'AgACAgIAAxkBAAIFd2O8VemWZUvi979oJD2PjInubE8tAAK1xTEbImjpSWRVHfuoScnTAQADAgADcwADLQQ', 'c27': 'AgACAgIAAxkBAAIGGGO-n_pGLazhj-6B8cTdK7se9oc6AAK2xTEbImjpSec1BwEuh92rAQADAgADcwADLQQ'}

def check(id):
    ids_file = open('user_ids_db.txt', 'r')
    lines = ids_file.readlines()
    for line in lines:
        if id in line:
            return False
    ids_file.close()
    return True


def sub_kb():
    kbsub = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = types.KeyboardButton('Новый день')
    b2 = types.KeyboardButton('Отправить')
    b3 = types.KeyboardButton('Галя, отмена!')
    kbsub.add(b1, b2, b3)
    return kbsub


def kb():
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
    c28 = types.KeyboardButton('Домой\U0001F3E0')
    keyboard.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22,
                 c23, c24, c25, c26, c27, c28)
    return keyboard


def kb2():
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


def kb1():
    kbrd = [
        [types.KeyboardButton('Узнать расписание\U0001F4DA')],
        [types.KeyboardButton('Изменить любимый класс\U0001F504')],
        [types.KeyboardButton('Посмотреть замены\U0001F440')]
    ]
    markup4 = types.ReplyKeyboardMarkup(keyboard=kbrd, resize_keyboard=True, row_width=1)
    return markup4


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


def get_tt(day, class_id):
    query = f'SELECT {day} FROM {class_id}'
    cur.execute(query)
    lessons = cur.fetchall()
    les_new = []
    for les in lessons:
        a = str(les)
        les_new.append(a[2:-3])
    while True:
        try:
            b = les_new.index(' ')
            del (les_new[b])
        except Exception:
            return les_new


def tt_photo(class_id):
    id = photo_ids[class_id]
    return id
