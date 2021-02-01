import requests
import re
from bs4 import BeautifulSoup


# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}


class WeatherMaker:
    """Создает атрибуты для парсинга и словарь """

    def __init__(self):
        self.response = requests.get("https://darksky.net/forecast/50.5967,36.5878/si12/en")
        self.dict_weather = {}
        self.reg_precip = r'\b\w+\b'

    def parse_weather(self):
        """Ищет погоду, температуру и дату"""
        b = BeautifulSoup(self.response.text, "html.parser")
        list_of_names = b.findAll('a', {'class': "moreDetails"})
        list_of_values = b.find_all("span", {'class': "minTemp"})
        list_of_weather = b.findAll("div", {'class': "summary"})
        for date, temperature, precipitation in zip(list_of_names, list_of_values, list_of_weather):
            date2 = date['href']
            date3 = re.search(r'(\d{4})-(\d{1})-(\d{1,2})', date2).group()
            temperature = re.sub(r'\s', '', temperature.text)
            word = re.compile(r'\w+')
            number = re.compile(r'\d+')
            # precipitation2 = re.search(self.reg_precip, precipitation.text).group()
            w_1 = word.findall(precipitation.text)[0]
            test = bool(re.search(number, precipitation.text))
            if test:
                precipitation = w_1
            else:
                w_2 = word.findall(precipitation.text)[1]
                precipitation = w_1 + " " + w_2
            self.dict_weather.update({date3: {'погода': precipitation, 'температура': temperature[:2]}})

#тест

# weather = WeatherMaker()
# weather.parse_weather()
