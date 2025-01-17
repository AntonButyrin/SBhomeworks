# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

month_number = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


# Номер месяца получать от пользователя следующим образом
while True:
    try:
        user_input = int(input("Введите, пожалуйста, номер месяца: "))
        if user_input < 1 or user_input > 12:
            raise Exception
        month = int(user_input)
        print('Вы ввели', month)
        break
    except ValueError:
        print('Неверный формат')
    except Exception:
        print('Такого месяца не существует. Введите номер месяца от 1 до 12')

print(month_number[user_input])

# Зачёт!
