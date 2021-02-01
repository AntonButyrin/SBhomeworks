import simple_draw as sd

angle = 90


def hot_sun(angle):
    point_2 = sd.get_point(100, 500)
    sd.circle(center_position=point_2, radius=30, width=29)
    for _ in range(15):
        v = sd.get_vector(start_point=point_2, angle=angle, length=50, width=1)
        v.draw()
        angle += 30


point = sd.get_point(0, 500)


def animation_sun(angle):
    sd.start_drawing()
    sd.circle(center_position=point, radius=30, color=sd.background_color, width=29)
    for i in range(12):
        v = sd.get_vector(start_point=point, angle=angle, length=50, width=1)
        v.draw(color=sd.background_color)
        angle += 30
    point.x += 15
    point_2 = sd.get_point(point.x, point.y)
    sd.circle(center_position=point_2, radius=30, width=29)
    for i in range(12):
        v2 = sd.get_vector(start_point=point_2, angle=angle, length=50, width=2)
        v2.draw(color=sd.COLOR_YELLOW)
        angle += 30
    sd.finish_drawing()
