import simple_draw as sd
point = sd.get_point(10, 10)

top_point = sd.get_point(100, 50)
bottom_point = sd.get_point(0, 0)


def brick_wall():
    for i, y in enumerate(range(0, 50, point.y)):
        if i % 2 == 0:
            top_point.x = 120
            bottom_point.x = 50
        else:
            top_point.x = 100
            bottom_point.x = 0

        for x in enumerate(range(0, 100, point.x)):
            sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=sd.COLOR_GREEN, width=1)
            top_point.x += 50

        top_point.y += 50
        bottom_point.y += 50



