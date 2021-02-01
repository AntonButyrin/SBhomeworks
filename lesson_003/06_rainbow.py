# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

rainbow_colors = [
    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE
]

point = sd.get_point(50, 50)
point_2 = sd.get_point(350, 450)

for color in range(len(rainbow_colors)):
    point.x += 5
    point_2.x += 5
    sd.line(start_point=point, end_point=point_2, color=rainbow_colors[color], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(150, 50)
radius = 400

for color in range(len(rainbow_colors)):
    radius += 10
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[color], width=10)

sd.pause()

# Зачёт!
