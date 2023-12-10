from PIL import Image, ImageDraw, ImageFont
import datetime
breakfast = []
dinner = []
s = ' '
a = ' '


def add_breakfast(meals):
    i = 140
    menu_back = Image.open('backg.png')
    processed = ImageDraw.Draw(menu_back)
    main_font = ImageFont.truetype('Mon_Amour_One.ttf', 48)
    sec_font = ImageFont.truetype('Lifehack.ttf', 42)
    for m in meals:
        processed.text((60, i), text=m, fill=(0, 0, 0), font=sec_font)
        i += 50
    menu_back.save('backg1.png')
    return i


def add_dinner(dinner_meals, y):
    y += 20
    dinner_menu = Image.open('backg1.png')
    processed_d = ImageDraw.Draw(dinner_menu)
    main_font_d = ImageFont.truetype('Mon_Amour_One.ttf', 48)
    sec_font_d = ImageFont.truetype('Lifehack.ttf', 42)
    processed_d.text((315, y), 'Обед', fill=(0, 0, 0), font=main_font_d)
    y += 95
    for m_d in dinner_meals:
        processed_d.text((60, y), text=m_d, fill=(0, 0, 0), font=sec_font_d)
        y += 50
    dinner_menu.save('backg1.png')
    return 0


def add_date(date):
    full_menu = Image.open('backg1.png')
    processed_full = ImageDraw.Draw(full_menu)
    d_font = ImageFont.truetype('Lifehack.ttf', 32)
    processed_full.text((690, 950), text=date, fill=(0, 0, 0), font=d_font, anchor='rt')
    full_menu.save('backg1.png')
    return 0


def count_weekday():
    today = datetime.date.today()
    weekday = today.weekday()
    date = datetime.datetime.now()
    day_time = int(date.strftime('%H'))
    if day_time >= 15 and weekday < 4:
        menu_day = weekday + 1
    elif weekday > 4:
        with open("menu.txt", 'r') as f:
            lines = f.readlines()
            if int(lines[5]) > int(today.strftime('%d')):
                menu_day = 0
            else:
                menu_day = 4
    else:
        menu_day = weekday
    return menu_day

