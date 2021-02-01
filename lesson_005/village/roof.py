import simple_draw as sd


def window():
    point = [sd.get_point(200, 100), sd.get_point(200, 200), sd.get_point(300, 200), sd.get_point(300, 100)]
    sd.polygon(point_list=point, color=sd.COLOR_WHITE, width=0)


def roof():
    point = [sd.get_point(0, 250), sd.get_point(200, 250), sd.get_point(600, 250), sd.get_point(300, 450)]
    sd.polygon(point_list=point, color=sd.COLOR_WHITE, width=0)