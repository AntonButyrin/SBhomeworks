import os
import peewee
import sqlite3
from datetime import datetime

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)
if not os.path.isdir("workfiles"):
    os.mkdir("workfiles")
db = peewee.SqliteDatabase('workfiles/weatherdate.db')


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Weather(BaseTable):
    day = peewee.DateTimeField(primary_key=True)
    precipitation = peewee.CharField()
    temperature = peewee.CharField()


def add_to_data(days, precip, temper):
    weather, created = Weather.get_or_create(
        day=days,
        precipitation=precip,
        temperature=temper,
    )
    weather.save()


def view_date(before_input, after_input):
    # before_input = str(input("Введите день 'от' в формате ГОД-МЕСЯЦ-ДЕНЬ:>  "))
    # after_input = str(input("Введите день 'до' в формате ГОД-МЕСЯЦ-ДЕНЬ:>  "))
    before = datetime.strptime(before_input, "%Y-%m-%d")
    after = datetime.strptime(after_input, "%Y-%m-%d")
    for data in Weather.select().where(Weather.day.between(before, after)):
        print(data.day, data.temperature)


def all_views():
    for data in Weather.select():
        print(data.day,  data.temperature, data.precipitation)

#
# db.create_tables([Weather], safe=True)
