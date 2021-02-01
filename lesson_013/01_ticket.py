# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


import argparse

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/ticket_template.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('ofont.ru_Primus.ttf', size=20)
names = input('Введите ФИО: ')
froms = input("Откуда летим?: ")
tos = input('Куда летим?: ')
times = input('День?: ')


def make_ticket(fio=names, from_=froms, to=tos, date=times):
    draw.text((45, 125), fill='#1C0606', text=fio, font=font, spacing=15)
    draw.text((45, 195), fill='#1C0606', text=from_, font=font, spacing=15)
    draw.text((45, 262), fill='#1C0606', text=to, font=font, spacing=15)
    draw.text((285, 262), fill='#1C0606', text=date, font=font, spacing=15)
    image.save('probe.png')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ticket')
    parser.add_argument('-a', dest=names, help='Need write your: Name, Middle Name, Last Name')
    parser.add_argument('-b', dest=froms, help='Need write where are you from')
    parser.add_argument('-c', dest=tos, help='Need write where you are going')
    make_ticket(fio=names, from_=froms, to=tos)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

# Зачёт!
