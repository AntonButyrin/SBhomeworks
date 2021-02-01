# -*- coding: utf-8 -*-
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.
import simple_draw as sd

from lesson_005.village.raindbow_module import raindbow, raindbow_animation
from lesson_005.village.roof import window, roof
from lesson_005.village.smile import smile_face
from lesson_005.village.snowflake import snowflake_drop
from lesson_005.village.sun import animation_sun
from lesson_005.village.three import threes
from lesson_005.village.wall import brick_wall

sd.resolution = (1250, 600)

angle = 90


# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
def animation():
    raindbow()
    brick_wall()
    window()
    roof()
    smile_face()
    threes()
    sd.take_background()
    while True:
        snowflake_drop()
        animation_sun(angle=angle)
        raindbow_animation()
        sd.sleep(0.1)


animation()

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# Зачёт!
