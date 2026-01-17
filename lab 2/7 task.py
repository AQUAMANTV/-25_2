sum_ = 0
n = 1
max_sum = 250


while True:
    if sum_ > max_sum:
        break
    sum_ += n
    n += 1
    print("Ещё считаю ...", sum_)

print("Количество чисел: ", n)
