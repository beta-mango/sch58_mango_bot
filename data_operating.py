import sqlite3
from aiogram import types
connection = sqlite3.connect('utils/ttable.db')
cur = connection.cursor()
photo_ids = {'c01': 'AgACAgIAAxkBAAIFRWO8VUPOUOVdgdwQzwc4LYQG8voxAAKYxTEbImjpSTLe0VHAZnWcAQADAgADcwADLQQ', 'c02': 'AgACAgIAAxkBAAIFR2O8VUigA8Ye98Ip57m1ne24HZWlAAKcxTEbImjpSZswEevHSc8AAQEAAwIAA3MAAy0E', 'c03': 'AgACAgIAAxkBAAIFSWO8VUw5g3EBWoYvDZ646w8XFgF3AAKdxTEbImjpSVtbuGg_hxdDAQADAgADcwADLQQ', 'c04': 'AgACAgIAAxkBAAIFS2O8VVT65ZG04fxNMTMLmlHoIr9FAAKexTEbImjpSf8gQ-39SbyjAQADAgADcwADLQQ', 'c05': 'AgACAgIAAxkBAAIFTWO8VVu2qeriYTEfXdM6jKz-nPmQAAKfxTEbImjpSV_Ddtl7J_20AQADAgADcwADLQQ', 'c06': 'AgACAgIAAxkBAAIFT2O8VWi3ESfFu1-2VeudJzDXUsDNAAKgxTEbImjpSQNBNJ2CChJQAQADAgADcwADLQQ', 'c07': 'AgACAgIAAxkBAAIFUWO8VW56M5tVZgJCpWQU6PXGtR8VAAKixTEbImjpSdUOnVgYAbRLAQADAgADcwADLQQ', 'c08': 'AgACAgIAAxkBAAIFU2O8VXI0tptHTGMn5ly3JCye1H9BAAKjxTEbImjpSX15xKLOxOmTAQADAgADcwADLQQ', 'c09': 'AgACAgIAAxkBAAIFVWO8VXYknfs1Mts1t20rjBKUTGTnAAKkxTEbImjpSVr4Dspk51rLAQADAgADcwADLQQ', 'c10': 'AgACAgIAAxkBAAIFV2O8VX7dD2ywIiXj7zElZzxhVqaNAAKlxTEbImjpSTpDcfsXwsniAQADAgADcwADLQQ', 'c11': 'AgACAgIAAxkBAAIFWWO8VYV68WYe1zChW39httgzn_uxAAKnxTEbImjpSdwAASr_cyCMSAEAAwIAA3MAAy0E', 'c12': 'AgACAgIAAxkBAAIFW2O8VY14VPpRGwzF1PB5YZF7X9kuAAKmxTEbImjpSdSSnHhNhNejAQADAgADcwADLQQ', 'c13': 'AgACAgIAAxkBAAIFXWO8VZOvwiqM4Jj23FxwjPgbI194AAKoxTEbImjpSfaX3xwd4SENAQADAgADcwADLQQ', 'c14': 'AgACAgIAAxkBAAIFX2O8VZdxKtkBJ70x_e7mZPDVEAn7AAKpxTEbImjpSZbJAAGE3hSm8QEAAwIAA3MAAy0E', 'c15': 'AgACAgIAAxkBAAIFYWO8VZwmmV-dHi5l737p0uUl6kyfAAKqxTEbImjpSVhwa-27oEqNAQADAgADcwADLQQ', 'c16': 'AgACAgIAAxkBAAIFY2O8VaEN0NeWZVqFUP5AhtVaF8IJAAKrxTEbImjpSdvKrGU7BC1KAQADAgADcwADLQQ', 'c17': 'AgACAgIAAxkBAAIFZWO8VanhoRvV7KiGO7Kk0IhccG8lAAKsxTEbImjpSYYphkx01ZVUAQADAgADcwADLQQ', 'c18': 'AgACAgIAAxkBAAIFZ2O8Va2sdzXJPSxutmRrqHclMHOEAAKtxTEbImjpSQv5x5b3yNc5AQADAgADcwADLQQ', 'c19': 'AgACAgIAAxkBAAIFaWO8VbOh5lO3IZ6QwY9msPe3UwwEAAKuxTEbImjpSbG0ZEpYQIMeAQADAgADcwADLQQ', 'c20': 'AgACAgIAAxkBAAIFa2O8VcMrzEZFC0rpw9VLyuxoDQABFQACr8UxGyJo6UlwzWBlzNQSgAEAAwIAA3MAAy0E', 'c21': 'AgACAgIAAxkBAAIFbWO8VclF9JxviYkhbIZMDtfIm1jAAAKwxTEbImjpSXyfWxLHDo_9AQADAgADcwADLQQ', 'c22': 'AgACAgIAAxkBAAIFb2O8Vc2VbE_h5nucPp0AAeBnVh1IJQACscUxGyJo6UnWUlk9jciYYgEAAwIAA3MAAy0E', 'c23': 'AgACAgIAAxkBAAIFcWO8VdTzKCh6mbx_TSuJy0rZlNNsAAKyxTEbImjpSWEBdTVitwmCAQADAgADcwADLQQ', 'c24': 'AgACAgIAAxkBAAIFc2O8VdyEw6XWa2qJD88r3n8xaw0UAAKzxTEbImjpSVqsQHSXXNh0AQADAgADcwADLQQ', 'c25': 'AgACAgIAAxkBAAIFdWO8VeB9OSQ7i7eztZ4eRgABX6GqdgACtMUxGyJo6Uk52jhahcBJmgEAAwIAA3MAAy0E', 'c26': 'AgACAgIAAxkBAAIFd2O8VemWZUvi979oJD2PjInubE8tAAK1xTEbImjpSWRVHfuoScnTAQADAgADcwADLQQ', 'c27': 'AgACAgIAAxkBAAIGGGO-n_pGLazhj-6B8cTdK7se9oc6AAK2xTEbImjpSec1BwEuh92rAQADAgADcwADLQQ'}
connection2 = sqlite3.connect('utils/configuration.db')
cur2 = connection2.cursor()


def check(id):
    ids_file = open('user_ids_db.txt', 'r')
    lines = ids_file.readlines()
    for line in lines:
        if id in line:
            return False
    ids_file.close()
    return True


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
            break
    while True:
        try:
            b = les_new.index('-')
            del (les_new[b])
            les_new.insert(b, ' ')
        except Exception:
            return les_new


def get_information(telegram_id):
    cur2.execute(f'SELECT * FROM user_data WHERE tg_id = {telegram_id}')
    info_tuple = cur2.fetchall()
    a, b, c, d = info_tuple[0]
    info = [a, b, c, d]
    return info


def update_format(tg_id, new_format):
    data = (new_format, tg_id)
    cur2.execute(f'UPDATE user_data SET ttable_format = ? WHERE tg_id = ?', data)
    connection2.commit()


def update_role(tg_id, class_id, new_role):
    data = (new_role, tg_id)
    cur2.execute(f'UPDATE user_data SET user_role = ? WHERE tg_id = ?', data)
    data2 = (class_id, tg_id)
    cur2.execute(f'UPDATE user_data SET class_id = ? WHERE tg_id = ?', data2)
    connection2.commit()
    with open('user_ids_db.txt', 'r') as file_ids:
        lines = file_ids.readlines()
        for line in lines:
            if tg_id in line:
                lines.remove(line)
                break
    lines.append(class_id + tg_id + '\n')
    with open('user_ids_db.txt', 'w') as f:
        f.writelines(lines)


def update_class(new, tg_id):
    data = (new, tg_id)
    cur2.execute(f'UPDATE user_data SET class_id = ? WHERE tg_id = ?', data)
    connection2.commit()


def update_teacher(teacher_id, tg_id):
    data = (teacher_id, tg_id)
    cur2.execute(f'UPDATE user_data SET class_id = ? WHERE tg_id = ?', data)
    connection2.commit()


def save_information(class_id, tg_id, user_role):
    data_tuple = (class_id, tg_id, 'text', user_role)
    cur2.execute('INSERT INTO user_data(class_id, tg_id, ttable_format, user_role) VALUES(?, ?, ?, ?);', data_tuple)
    connection2.commit()


def tt_photo(class_id):
    id = photo_ids[class_id]
    return id

