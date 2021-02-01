# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from lesson_005.district.central_street.house1.room1 import folks as cenho1ro1
from lesson_005.district.central_street.house1.room2 import folks as cenho1ro2
from lesson_005.district.central_street.house2.room1 import folks as cenho2ro1
from lesson_005.district.central_street.house2.room2 import folks as cenho2ro2
from lesson_005.district.soviet_street.house1.room1 import folks as sovho1ro1
from lesson_005.district.soviet_street.house1.room2 import folks as sovho1ro2
from lesson_005.district.soviet_street.house2.room1 import folks as sovho2ro1
from lesson_005.district.soviet_street.house2.room2 import folks as sovho2ro2
all_houses_sum = cenho1ro1 + cenho1ro2 + cenho2ro1 + cenho2ro2 + sovho1ro2 + sovho1ro1 + sovho2ro1 + sovho2ro2
print("На районе живут: ", ','.join(all_houses_sum))

# Зачёт!
