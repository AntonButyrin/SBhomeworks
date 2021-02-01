import simple_draw as sd
import random

rainbow_colors = [
    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE
]

point = sd.get_point(90, 50)


def raindbow():
    radius = 700
    for color in range(len(rainbow_colors)):
        radius += 10
        sd.circle(center_position=point, radius=radius, color=rainbow_colors[color], width=10)


def raindbow_animation():
    sd.start_drawing()
    radius = 700
    for color in range(len(rainbow_colors)):
        radius += 10
        sd.circle(center_position=point, radius=radius, color=random.choice(rainbow_colors), width=10)
    sd.finish_drawing()
