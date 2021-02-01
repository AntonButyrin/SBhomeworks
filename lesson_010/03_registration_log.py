# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class Ages(ValueError):
    pass


#  Название iter не нужно использовать для переменных,
#  это слово зарезервировано для встроенной функции.
def file(_iter):
    constant1, constant2, constant3 = _iter.split()
    constant3 = int(constant3)
    if not constant1.isalpha():
        raise NotNameError
    elif '@' not in constant2 or '.' not in constant2:
        raise NotEmailError
    elif constant3 <= 10 or constant3 >= 99:
        raise Ages


file_reg = 'registrations.txt'
file_bad = 'registrations_bad.log'
file_good = 'registrations_good.log'

with open(file_bad, 'a', encoding='utf-8') as f, open(file_good, 'a', encoding='utf-8')as f2, open(file_reg, 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            file(line)
        except Ages as exc:
            print(f'Найдена ошибка - возраст {exc} в строке {line}')
            f.write(line + '\n')
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Нехватает полей  {exc} в строке {line}')
                f.write(line + '\n')
            else:
                print(f'Неправильно расположены поля {exc} в  строке {line}')
                f.write(line + '\n')
        except NotNameError as exc:
            print(f'Найдена ошибка - имя {exc} в строке {line}')
            f.write(line + '\n')
        except NotEmailError as exc:
            print(f'Найдена ошибка - почта {exc} в строке {line}')
            f.write(line + '\n')
        else:
            f2.write(line + '\n')

# Зачёт!
