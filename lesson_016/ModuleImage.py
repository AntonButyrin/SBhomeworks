import cv2
import os
import copy
from random import randint
from PIL import Image, ImageDraw
import numpy


# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому


class ImageMaker:
    """Создает атрибуты для картинки"""

    def __init__(self):

        self.image_cv2 = 'python_snippets/external_data/probe.jpg'
        self.precip = str()
        self.temp = str()
        self.date = str()
        self.name = 'test_weather'
        self.dict = {
            'rain': {'image': 'python_snippets/external_data/weather_img/rain.jpg', 'color': (0, 0, 225)},
            'snow': {'image': 'python_snippets/external_data/weather_img/snow.jpg', 'color': (0, 127, 255)},
            'clear': {'image': 'python_snippets/external_data/weather_img/sun.jpg', 'color': (255, 179, 0)},
            'cloudy': {'image': 'python_snippets/external_data/weather_img/cloud.jpg', 'color': (128, 128, 128)}
        }
        # self.image_cv =

    def view_image(self):
        """Создает картинку и пишет на ней текст"""
        if not os.path.isdir("blank_files"):
            os.mkdir("blank_files")
        self.paste_picture(self.image_cv2)
        self.image_cv1 = copy.copy(cv2.imread('blank_files/blank.jpg'))
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(self.image_cv1, self.date, (110, 100), font, 1, color=(0, 0, 255), thickness=3)
        cv2.putText(self.image_cv1, self.precip, (30, 160), font, 1, color=(0, 0, 255), thickness=2)
        cv2.putText(self.image_cv1, self.temp, (30, 190), font, 1, color=(0, 0, 255), thickness=2)
        if not os.path.isdir("images"):
            os.mkdir("images")
        cv2.imwrite(f'images/{self.date}.jpg', self.image_cv1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def text_split(self, text, pog, temper):
        """Дробит входящий словарь на отдельные элементы"""
        self.date = text
        self.precip = pog
        self.temp = temper

    def paste_picture(self, picture):
        """Выбирает картинку и накладывает её"""
        try:
            img_to_paste = Image.open(picture)
            draw = ImageDraw.Draw(img_to_paste)
            choice = self.precipitation()
            img_to_paste2 = Image.open(self.dict[choice]["image"])
            r = int(self.dict[choice]['color'][0])
            g = int(self.dict[choice]['color'][1])
            b = int(self.dict[choice]['color'][2])
            for i in range(img_to_paste.size[0]):
                draw.line((i, 0, i, 512), fill=(r, g, b), width=2)
                if r < 255:
                    r += 1
                if g < 255:
                    g += 1
                if b < 255:
                    b += 1
            img_to_paste.paste(img_to_paste2)
            img_to_paste.save('blank_files/blank.jpg')
        except KeyError:
            print("погода не определена")

    def precipitation(self):
        if 'Snow' in self.precip:
            return 'snow'
        elif 'Rain' in self.precip or 'rainy' in self.precip:
            return 'rain'
        elif 'Clear' in self.precip or 'Possible' in self.precip:
            return 'clear'
        elif 'cloudy' in self.precip or 'Foggy' in self.precip:
            return 'cloudy'
