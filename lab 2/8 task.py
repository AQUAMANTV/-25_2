list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

even_count = 0   # чётные
odd_count = 0    # нечётные

for num in list_:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print("Четных чисел больше")
elif odd_count > even_count:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")