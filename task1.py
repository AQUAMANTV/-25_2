import random

# ---------- Классы ----------

class Book:
    """
    Базовый класс для всех книг.

    Атрибуты (доступны только для чтения):
        name (str): название книги.
        author (str): автор.
    """

    def __init__(self, name: str, author: str) -> None:
        self._name = None
        self._author = None
        # используем сеттеры для проверки
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Название должно быть непустой строкой")
        self._name = value.strip()

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Автор должен быть непустой строкой")
        self._author = value.strip()

    def __str__(self) -> str:
        return f'Книга "{self.name}" автора {self.author}'

    def __repr__(self) -> str:
        return f"Book(name={self.name!r}, author={self.author!r})"


class Paperback(Book):
    """
    Бумажная книга.
    Добавляет атрибут pages (количество страниц) с проверкой.
    """

    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self.pages = pages   # используем сеттер

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __repr__(self) -> str:
        return f"Paperback(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """
    Аудиокнига.
    Добавляет атрибут duration (длительность в часах) с проверкой.
    """

    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self) -> str:
        # Перегружаем, чтобы включить информацию о длительности
        return f'Аудиокнига "{self.name}" автора {self.author}, длительность {self.duration} ч.'

    def __repr__(self) -> str:
        return f"AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# ---------- Вспомогательные функции для меню ----------

def clear_screen():
    """Очистка экрана."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title: str):
    """Печатает заголовок с рамкой."""
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def print_books(books):
    """Выводит нумерованный список книг."""
    if not books:
        print("   Список пуст.")
        return
    for i, book in enumerate(books):
        icon = "📖" if isinstance(book, Paperback) else "🎧"
        print(f"{i+1:2}. {icon} {book}")

def get_int_input(prompt: str, min_val=None, max_val=None) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Значение должно быть не меньше {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Значение должно быть не больше {max_val}.")
                continue
            return val
        except ValueError:
            print("Ошибка: введите целое число.")

def get_float_input(prompt: str, min_val=None, max_val=None) -> float:
    """Безопасный ввод числа с плавающей точкой."""
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Значение должно быть не меньше {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Значение должно быть не больше {max_val}.")
                continue
            return val
        except ValueError:
            print("Ошибка: введите число.")

def get_string_input(prompt: str, allow_empty=False) -> str:
    """Ввод строки с возможностью проверки на пустоту."""
    while True:
        s = input(prompt).strip()
        if not allow_empty and s == "":
            print("Строка не может быть пустой.")
        else:
            return s


# ---------- Генерация случайных книг ----------

FIRST_NAMES = ["Лев", "Фёдор", "Антон", "Мария", "Александр", "Иван", "Елена"]
LAST_NAMES = ["Толстой", "Достоевский", "Чехов", "Пушкина", "Грибоедов", "Тургенев", "Ахматова"]
TITLES = ["Война и мир", "Преступление и наказание", "Анна Каренина", "Евгений Онегин",
          "Герой нашего времени", "Мёртвые души", "Отцы и дети", "Идиот"]

def generate_random_book(book_type: str = None):
    """Генерирует случайную книгу указанного типа. Если тип не указан, выбирается случайно."""
    if book_type is None:
        book_type = random.choice(["Paperback", "AudioBook"])
    author = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    title = random.choice(TITLES)
    if book_type == "Paperback":
        pages = random.randint(50, 1200)
        return Paperback(title, author, pages)
    else:  # AudioBook
        duration = round(random.uniform(1.0, 30.0), 1)
        return AudioBook(title, author, duration)

def generate_multiple_books(count: int):
    """Генерирует список из count случайных книг."""
    return [generate_random_book() for _ in range(count)]


# ---------- Подменю работы с выбранной книгой ----------

def book_detail_menu(book):
    """Меню для взаимодействия с конкретной книгой."""
    while True:
        clear_screen()
        print_header(f"Детальный просмотр: {book}")
        print(f"Тип: {'Бумажная' if isinstance(book, Paperback) else 'Аудиокнига'}")
        print(f"Название: {book.name} (изменить нельзя)")
        print(f"Автор: {book.author} (изменить нельзя)")
        if isinstance(book, Paperback):
            print(f"Страниц: {book.pages}")
        elif isinstance(book, AudioBook):
            print(f"Длительность: {book.duration} ч.")
        print("\nДоступные действия:")
        print("1. Показать str")
        print("2. Показать repr")
        if isinstance(book, Paperback):
            print("3. Изменить количество страниц")
        elif isinstance(book, AudioBook):
            print("3. Изменить длительность")
        print("4. Попытаться изменить название (демонстрация ошибки)")
        print("5. Вернуться к списку")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            input(str(book) + "\nНажмите Enter...")
        elif choice == "2":
            input(repr(book) + "\nНажмите Enter...")
        elif choice == "3":
            try:
                if isinstance(book, Paperback):
                    new_pages = get_int_input("Новое количество страниц: ", min_val=1)
                    book.pages = new_pages
                    print("Количество страниц обновлено.")
                elif isinstance(book, AudioBook):
                    new_dur = get_float_input("Новая длительность (ч): ", min_val=0.1)
                    book.duration = new_dur
                    print("Длительность обновлена.")
                else:
                    print("Для этого типа книг нет изменяемых параметров.")
            except ValueError as e:
                print(f"Ошибка: {e}")
            input("Нажмите Enter...")
        elif choice == "4":
            print("Пытаемся изменить название...")
            try:
                book.name = "Новое название"
            except AttributeError as e:
                print(f"Ожидаемая ошибка (нет setter): {e}")
            except ValueError as e:
                print(f"Ошибка валидации: {e}")
            input("Нажмите Enter...")
        elif choice == "5":
            break
        else:
            print("Неверный ввод.")
            input("Нажмите Enter...")


# ---------- Главное меню ----------

def main_menu():
    books = []
    # Добавим несколько демо-книг
    books.append(Paperback("Война и мир", "Лев Толстой", 1300))
    books.append(AudioBook("1984", "Джордж Оруэлл", 11.5))
    books.append(Paperback("Преступление и наказание", "Фёдор Достоевский", 672))

    while True:
        clear_screen()
        print_header("БИБЛИОТЕКА КНИГ (задание 4: наследование и property)")
        print("Список книг:")
        print_books(books)
        print("\nМеню:")
        print("1. Добавить новую книгу")
        print("2. Сгенерировать случайные книги")
        print("3. Выбрать книгу для детального просмотра (по номеру)")
        print("4. Удалить книгу (по номеру)")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_book_menu(books)
        elif choice == "2":
            generate_books_menu(books)
        elif choice == "3":
            select_book_menu(books)
        elif choice == "4":
            delete_book_menu(books)
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод.")
            input("Нажмите Enter...")

def add_book_menu(books):
    """Меню добавления новой книги (ручной ввод)."""
    clear_screen()
    print_header("Добавление новой книги")
    print("Выберите тип:")
    print("1. Бумажная (Paperback)")
    print("2. Аудиокнига (AudioBook)")
    type_choice = input("Ваш выбор (1/2): ").strip()

    try:
        name = get_string_input("Название: ")
        author = get_string_input("Автор: ")

        if type_choice == "1":
            pages = get_int_input("Количество страниц: ", min_val=1)
            book = Paperback(name, author, pages)
        elif type_choice == "2":
            duration = get_float_input("Длительность (часы): ", min_val=0.1)
            book = AudioBook(name, author, duration)
        else:
            print("Неверный выбор типа.")
            input("Нажмите Enter...")
            return

        books.append(book)
        print(f"Книга '{book.name}' успешно добавлена!")
    except ValueError as e:
        print(f"Ошибка при создании: {e}")
    input("Нажмите Enter...")

def generate_books_menu(books):
    """Меню генерации случайных книг."""
    clear_screen()
    print_header("Генерация случайных книг")
    count = get_int_input("Сколько книг сгенерировать? ", min_val=1, max_val=20)
    new_books = generate_multiple_books(count)
    books.extend(new_books)
    print(f"Сгенерировано {count} книг.")
    input("Нажмите Enter...")

def select_book_menu(books):
    """Выбор книги по номеру для детального просмотра."""
    if not books:
        print("Список пуст. Нечего выбирать.")
        input("Нажмите Enter...")
        return
    print_books(books)
    idx = get_int_input("Введите номер книги: ", min_val=1, max_val=len(books)) - 1
    book_detail_menu(books[idx])

def delete_book_menu(books):
    """Удаление книги по номеру."""
    if not books:
        print("Список пуст. Нечего удалять.")
        input("Нажмите Enter...")
        return
    print_books(books)
    idx = get_int_input("Введите номер книги для удаления: ", min_val=1, max_val=len(books)) - 1
    removed = books.pop(idx)
    print(f"Книга '{removed.name}' удалена.")
    input("Нажмите Enter...")

if __name__ == "__main__":
    main_menu()