# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
from lesson_005.room_1 import folks as folks_r1
from lesson_005.room_2 import folks as folks_r2
folks_room_1 = ",".join(folks_r1)
folks_room_2 = ",".join(folks_r2)
print("В комнате room_1 живут: ", folks_room_1)
print("В комнате room_2 живёт: ", folks_room_2)

# Зачёт!
