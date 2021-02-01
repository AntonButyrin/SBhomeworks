import random
import simple_draw as sd

list_down = []
use_list = []


def create_snowflake(counter):
    snowflake_1 = []
    a = 0
    while a <= counter:
        random_number = sd.random_number(200, 1000)
        random_number_2 = sd.random_number(800, 1000)
        b = (random_number, random_number_2)
        snowflake_1.extend(b)
        use_list.append(random.sample(snowflake_1, 2))
        a += 1


def painting_snowflake(color):
    for x, y in use_list:
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=50, color=color)


def shift():
    for i, (x, y) in enumerate(use_list):
        drop = int(use_list[i][1])
        if drop > 0:
            y -= 10
            x -= 10
        use_list[i][1] = y
        use_list[i][0] = x


def list_fall():
    index_list = []
    for i, (x, y) in enumerate(use_list):
        drop = int(use_list[i][1])
        if drop < 0:
            list_down.append(y)
            index_list.append(list_down.index(y))
    return index_list


def delete_snowflake(index_list):
    return index_list.clear()
