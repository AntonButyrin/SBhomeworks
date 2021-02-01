import simple_draw as sd

color = sd.COLOR_DARK_RED
radius = 50
radius_eyes = 6


def smile_face():
    def smile(x, y, coloring):
        sd.circle(center_position=point, radius=radius, color=coloring, width=1)
        point.x += 10
        point.y += 10
        r_eyes_z = sd.get_point(point.x, point.y)

        sd.circle(center_position=r_eyes_z, radius=radius_eyes, color=coloring, width=1)
        point.x -= 40
        point.y += 0
        l_eyes_z = sd.get_point(point.x, point.y)

        sd.circle(center_position=l_eyes_z, radius=radius_eyes, color=coloring, width=1)
        point.x -= 0
        point.y -= 40
        l_month_z = sd.get_point(point.x, point.y)

        point.x += 40
        point.y += 0
        r_month_z = sd.get_point(point.x, point.y)
        sd.line(start_point=l_month_z, end_point=r_month_z, color=coloring, width=4)

    for _ in range(1):
        point = sd.get_point(250, 150)
        smile(x=point.x, y=point.y, coloring=color)
