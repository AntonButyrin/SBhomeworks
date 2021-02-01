import simple_draw as sd

N = 20

x_list = []

for m in range(0, 500, 30):
    random_number = sd.random_number(200, 1000)
    x_list.append(random_number)

y_list = []

for n in range(0, 500):
    random_number = sd.random_number(0, 1000)
    y_list.append(random_number)


def snowflake_drop():
    sd.start_drawing()
    for i, (x, y) in enumerate(zip(x_list, y_list)):
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=50, color=sd.background_color)
        sd.draw_background()
        if y > 0:
            y -= 10
            x -= 10
        else:
            x = sd.random_number(500, 1000)
            y = sd.random_number(500, 1000)
        y_list[i] = y
        x_list[i] = x
        point_2 = sd.get_point(x, y)
        sd.snowflake(center=point_2, length=50, color=sd.COLOR_WHITE)
        if sd.user_want_exit():
            break
    sd.finish_drawing()
