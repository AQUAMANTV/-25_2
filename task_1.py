numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)

total_sum = 0
count_without_none = 0
for num in numbers:
    if num is not None:
        total_sum += num
        count_without_none += 1

total_count = len(numbers)
average = total_sum / total_count
numbers[none_index] = average
print("Измененный список:",numbers)