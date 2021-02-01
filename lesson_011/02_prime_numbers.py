# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number1 in range(2, n + 1):
        for prime in prime_numbers:
            if number1 % prime == 0:
                break
        else:
            prime_numbers.append(number1)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.number_counter = 2
        return self

    def __next__(self):
        for number_iter in range(self.number_counter, self.n + 1):
            for prime in self.prime_numbers:
                if number_iter % prime == 0:
                    break
            else:
                self.prime_numbers.append(number_iter)
                self.number_counter = number_iter
                return number_iter
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number1 in range(2, n + 1):
        for prime in prime_numbers:
            if number1 % prime == 0:
                break
        else:
            prime_numbers.append(number1)
            yield number1


for number in prime_numbers_generator(n=1000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def pal_func(numb):
    numb = str(numb)
    if numb == numb[::-1]:
        return numb


def luck_func(numb):
    for char in range(numb, numb + 1):
        str_numb = list(str(numb))
        first_number = int(str_numb[0])
        second_number = int(str_numb[1])
        last_number = int(str_numb[-1])
        pre_last_number = int(str_numb[-2])
        middle = len(str_numb) // 2
        if str_numb[:middle] == str_numb[-middle:]:
            return str_numb
        elif first_number + second_number == last_number + pre_last_number:
            return str_numb


list_numbers = (737, 244, 192, 545, 92083)

a = filter(pal_func, list_numbers)
b = filter(luck_func, list_numbers)
print(list(a))
print(list(b))


#  почему у меня не проходит проверка, а сразу выкидывает резуьтат(ко всему прочему еще и не проверенный),
#  причем он еще и дублируемый.
#  Ведь список передан. Циклом идем по списку и если у нас "cycle" == True он возвращает цифру.
#  Сгенерированное число нужно возвращать только если все проверк вернут True.


def luck_func(numb):
    try:
        for char in range(numb, numb + 1):
            str_numb = list(str(numb))
            a1 = int(str_numb[0])
            b1 = int(str_numb[1])
            c1 = int(str_numb[-1])
            d1 = int(str_numb[-2])
            middle = len(str_numb) // 2
            if str_numb[:middle] == str_numb[-middle:]:
                return str_numb
            elif a1 + b1 == c1 + d1:
                return str_numb
    except IndexError:
        return numb


def prime_numbers_generator(n, func):
    prime_numbers = []
    for number1 in range(2, n + 1):
        for prime in prime_numbers:
            if number1 % prime == 0:
                break
        else:
            prime_numbers.append(number1)
            for cycle in func:
                if not cycle(numb=number1):
                    break
            else:
                yield number1


list_func = [pal_func, luck_func]

for number in prime_numbers_generator(n=100000, func=list_func):
    print(number)

# Зачёт!
