import sqlite3
from aiogram import types
connection = sqlite3.connect('utils/ttable.db')
cur = connection.cursor()
photo_ids = {'c01': 'AgACAgIAAxkBAALgkmVzQEZJSrs1WsBtswaLRhuiqL5EAALY1TEbsTKZS5wnn48Xme6QAQADAgADcwADMwQ', 'c02': 'AgACAgIAAxkBAALgk2VzQEohCu9Xd31Fmme_YI0-VShqAALZ1TEbsTKZS57H5k4Y3zT4AQADAgADcwADMwQ', 'c03': 'AgACAgIAAxkBAALglGVzQE9mFSbqITb-TCrQ9up1G2S5AALa1TEbsTKZS-AxVtyzzxGJAQADAgADcwADMwQ', 'c04': 'AgACAgIAAxkBAALglWVzQFIFSZMweyUka1nPJTykCmdLAALb1TEbsTKZS154B9S_xEdGAQADAgADcwADMwQ', 'c05': 'AgACAgIAAxkBAALglmVzQFYBF11AzsyY-ZJqZbG99EmaAALc1TEbsTKZS4vUUTVEg8oTAQADAgADcwADMwQ', 'c06': 'AgACAgIAAxkBAALgl2VzQF7gb7j9XkFSEJrRovdh9nScAALd1TEbsTKZS9xe995f4RXoAQADAgADcwADMwQ', 'c07': 'AgACAgIAAxkBAALgmGVzQGL3n7YjRXjxg2X8ZnYErzJQAALe1TEbsTKZSwlIe5JLLhEgAQADAgADcwADMwQ', 'c08': 'AgACAgIAAxkBAALgmWVzQGbmrWFArUBaqxhFXkQmPZ5vAALf1TEbsTKZS3WIw2o1RzkmAQADAgADcwADMwQ', 'c09': 'AgACAgIAAxkBAALgmmVzQGuhYllp6R5y709toPM51tv2AALg1TEbsTKZS_Jg0G5knU9WAQADAgADcwADMwQ', 'c10': 'AgACAgIAAxkBAALgm2VzQHHr5DM6dWY04XFgPNWps5ZPAALh1TEbsTKZS7FIfckT-CQjAQADAgADcwADMwQ', 'c11': 'AgACAgIAAxkBAALgnGVzQHaxN9fYWLooIrXWg5ZsThm2AALk1TEbsTKZS2-4eDvxRE7FAQADAgADcwADMwQ', 'c12': 'AgACAgIAAxkBAALgnWVzQHvdgEOXpLatxTW5hiUHVX4wAALl1TEbsTKZS2cjUO29brWkAQADAgADcwADMwQ', 'c13': 'AgACAgIAAxkBAALgnmVzQIHRvwABmfGpRczo7vY7mGiNKQAC5tUxG7EymUs6janpzfKSMgEAAwIAA3MAAzME', 'c14': 'AgACAgIAAxkBAALgn2VzQIc4xaG_iFRNAjzQOZ7S5RnXAALn1TEbsTKZS8KTHkIaqat2AQADAgADcwADMwQ', 'c15': 'AgACAgIAAxkBAALgoGVzQIzt5otvVmhjRS60ddXnVvmbAALo1TEbsTKZS0V5Z5jsIOZmAQADAgADcwADMwQ', 'c16': 'AgACAgIAAxkBAALgoWVzQJGmAAHJ0ldOEA4UtXLGqdTdxgAC6dUxG7EymUtxDWQkQkYqvgEAAwIAA3MAAzME', 'c17': 'AgACAgIAAxkBAALgomVzQJazm_3csts8jgh8W3pZlwvEAALq1TEbsTKZS6dL7EpxOHgfAQADAgADcwADMwQ', 'c18': 'AgACAgIAAxkBAALgo2VzQJvjtMmpVB6eugjDtPAbfo2FAALr1TEbsTKZS7Xh7g0GXvnkAQADAgADcwADMwQ', 'c19': 'AgACAgIAAxkBAALgpGVzQKA65b75kcuSUyH2hPekpYoYAALs1TEbsTKZS784YpA0nRrWAQADAgADcwADMwQ', 'c20': 'AgACAgIAAxkBAALgpWVzQKbsUx_UNRJySy1EWbBFNsOaAALt1TEbsTKZS0Pa1JIEmK0YAQADAgADcwADMwQ', 'c21': 'AgACAgIAAxkBAALgpmVzQKz_R2QKDbuJzmeYM0oU3ogXAALu1TEbsTKZS-_2eKsXmK3xAQADAgADcwADMwQ', 'c22': 'AgACAgIAAxkBAALgp2VzQLM5oWLvXDs2so8NTZ-1HvnUAALv1TEbsTKZS6V-BOjsze0SAQADAgADcwADMwQ', 'c23': 'AgACAgIAAxkBAALgqGVzQLgmKfkt1MgIe7MyGuKPosLfAALw1TEbsTKZSweyqorGX8oBAQADAgADcwADMwQ', 'c24': 'AgACAgIAAxkBAALgqWVzQL7eMXhH-6SuY5A4CxU9nmEdAALx1TEbsTKZS9LstQbQu3VSAQADAgADcwADMwQ', 'c25': 'AgACAgIAAxkBAALgqmVzQMNOjEJr_lIt5pjSVwxpytu6AALz1TEbsTKZSy5lRriW0u6JAQADAgADcwADMwQ', 'c26': 'AgACAgIAAxkBAALgq2VzQMhq3_1zcHXdfOaz61H3TIG0AAL11TEbsTKZS-tkTzZwjHMpAQADAgADcwADMwQ', 'c27': 'AgACAgIAAxkBAALhLWV0LXIWD96sJkbEOu-FBpMZ-fXWAAJ_0DEbzg2gS3zEbqVPzZ0oAQADAgADcwADMwQ'}
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
    data_tuple = (class_id, tg_id, 'photo', user_role)
    cur2.execute('INSERT INTO user_data(class_id, tg_id, ttable_format, user_role) VALUES(?, ?, ?, ?);', data_tuple)
    connection2.commit()


def tt_photo(class_id):
    id = photo_ids[class_id]
    return id

