import simple_draw as sd
point_triangle = sd.get_point(300, 300)
color = sd.COLOR_BLACK


def triangle(point, angle, length, coloring):
    now_point = point
    now_length = length
    for i in range(3):
        v = sd.get_vector(start_point=now_point, angle=angle, length=now_length, width=1)
        v.draw(color=coloring)
        now_point = v.end_point
        angle = angle + 120




triangle(point=point_triangle, angle=0, length=100, coloring=color)

sd.pause()
