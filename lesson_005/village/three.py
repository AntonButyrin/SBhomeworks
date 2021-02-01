import simple_draw as sd

root_point = sd.get_point(900, 0)

def threes():
    def branch(point, angle, length, delt):
        if length < 10:
            return
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()

        next_angle_right = angle - 30
        next_length_right = length * 0.75
        next_point_right = v1.end_point
        branch(point=next_point_right, angle=next_angle_right, length=next_length_right, delt=delt)

        v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v2.draw()

        next_length_left = length * 0.75
        next_angle_left = angle + 30
        next_point_left = v1.end_point
        branch(point=next_point_left, angle=next_angle_left, length=next_length_left, delt=delt)

    for delta in range(0, 51, 10):
        branch(point=root_point, angle=90, length=100, delt=delta)

