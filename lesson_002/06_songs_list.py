#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)


summ = (round(violator_songs_list[3][1], 0)
        + round(violator_songs_list[5][1], 0)
        + round(violator_songs_list[8][1], 0)
)
print('Три песни звучат ', summ, ' минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
first_song = violator_songs_dict['Sweetest Perfection']
second_song = violator_songs_dict['Policy of Truth']
third_song = violator_songs_dict['Blue Dress']
summ_song = first_song + second_song + third_song

print ("Эти песни ('Sweetest Perfection, 'Policy of Truth', 'Blue Dress') звучат "
      +  str (round (summ_song, 2)) + " минут")


other_song_first = violator_songs_dict["World in My Eyes"]
other_song_second = violator_songs_dict["Clean"]
other_song_third = violator_songs_dict["Waiting for the Night"]

summ_other_song = other_song_first + other_song_second + other_song_third

print ("Эти песни ('World in My Eyes, 'Clean', 'Waiting for the Night') звучат "
      +  str (round (summ_other_song)) + " минут")

# Зачёт!
