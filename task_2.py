disk_mb = 1.44
disk_bytes = disk_mb * 1024 * 1024
pages = 100          # страниц
lines_page = 50  # строк на странице
chars_line = 25  # символов в строке
bytes_char = 4   # байта на символ

# Общий объём одной книги в байтах
book_size_bytes = pages * lines_page * chars_line * bytes_char

# Вычисляем, сколько книг поместится на диск (целое число)
number_of_books = disk_bytes // book_size_bytes

# Выводим результат
print("Количество книг, помещающихся на дискету:" ,int(number_of_books))
