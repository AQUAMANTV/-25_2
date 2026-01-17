src = not False and True or False and not True

# Упрощение выражения по шагам:

# 1. Упростить оператор `not`:
#    not False → True
#    not True → False
#    Получаем: True and True or False and False

# 2. Упростить оператор `and` (выполняется до `or`):
#    True and True → True
#    False and False → False
#    Получаем: True or False

# 3. Упростить оператор `or`:
#    True or False → True

result = True  

print(src == result)  