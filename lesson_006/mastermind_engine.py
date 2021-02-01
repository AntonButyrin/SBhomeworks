import random

game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_four = []


def create_number():
    random.shuffle(game_list)
    if game_list[0] == 0:
        random_four.extend(game_list[1:5])
    else:
        random_four.extend(game_list[0:4])


def check(user_input):
    result = {"cow": 0, "bulls": 0}
    for i in range(4):
        if user_input[i] == random_four[i]:
            result["bulls"] += 1
        elif user_input[i] in random_four:
            result["cow"] += 1
    return result


def win():
    return random_four
