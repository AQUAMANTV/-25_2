class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (int): уникальный идентификатор книги.
        name (str): название книги.
        pages (int): количество страниц.
    """

    def __init__(self, id: int, name: str, pages: int) -> None:
        """
        Инициализирует экземпляр Book.

        Аргументы:
            id: целое положительное число.
            name: непустая строка.
            pages: целое положительное число.

        >>> b = Book(1, 'Война и мир', 1300)
        >>> b.name
        'Война и мир'
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID должен быть положительным целым числом")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает валидное Python-выражение для воссоздания объекта."""
        return f"Book(id={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        books (list[Book]): список книг в библиотеке.
    """

    def __init__(self, books: list[Book] | None = None) -> None:
        """
        Инициализирует библиотеку. Если список не передан, создаётся пустой.

        Аргументы:
            books: список объектов Book (по умолчанию None).

        >>> lib = Library()
        >>> lib.books
        []
        """
        if books is None:
            books = []
        if not all(isinstance(b, Book) for b in books):
            raise ValueError("Все элементы должны быть экземплярами Book")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для следующей добавляемой книги.

        Если библиотека пуста, возвращает 1.
        Иначе возвращает id последней книги + 1.

        >>> lib = Library([Book(5, 'Existing', 100)])
        >>> lib.get_next_book_id()
        6
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id: int) -> int:
        """
        Возвращает индекс книги в списке по её id.

        Аргументы:
            id: идентификатор книги.

        Возвращает:
            Индекс (целое число) в списке books.

        Исключения:
            ValueError: если книга с указанным id не найдена.

        >>> lib = Library([Book(3, 'Test', 50), Book(7, 'Example', 120)])
        >>> lib.get_index_by_book_id(7)
        1
        """
        for i, book in enumerate(self.books):
            if book.id == id:
                return i
        raise ValueError("Книги с запрашиваемым id не существуют")

    # Дополнительный метод для удобства удаления книги
    def remove_book_by_id(self, id: int) -> None:
        """Удаляет книгу по её идентификатору."""
        index = self.get_index_by_book_id(id)
        removed = self.books.pop(index)
        print(f"Книга '{removed.name}' (ID {removed.id}) удалена.")


def menu_library():
    """Интерактивное меню для управления библиотекой."""
    lib = Library()  # создаём пустую библиотеку
    print("=" * 50)
    print("Добро пожаловать в систему управления библиотекой!")
    print("=" * 50)

    while True:
        print("\n--- Главное меню библиотеки ---")
        print("1. Добавить новую книгу")
        print("2. Показать все книги")
        print("3. Найти индекс книги по ID")
        print("4. Удалить книгу по ID")      # опционально, для удобства
        print("5. Выход")
        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            add_book(lib)
        elif choice == "2":
            show_books(lib)
        elif choice == "3":
            find_index(lib)
        elif choice == "4":
            remove_book(lib)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1-5.")


def add_book(lib: Library):
    """Добавление новой книги в библиотеку."""
    print("\n--- Добавление новой книги ---")
    try:
        # ID генерируется автоматически
        next_id = lib.get_next_book_id()
        print(f"Будет присвоен ID: {next_id}")

        name = input("Введите название книги: ").strip()
        if not name:
            print("Ошибка: название не может быть пустым.")
            return

        pages_str = input("Введите количество страниц: ").strip()
        if not pages_str:
            print("Ошибка: количество страниц не указано.")
            return
        pages = int(pages_str)

        # Создаём книгу (конструктор сам проверит корректность)
        book = Book(next_id, name, pages)

        # Добавляем в библиотеку
        lib.books.append(book)
        print(f"Книга '{name}' успешно добавлена с ID {next_id}.")

    except ValueError as e:
        print(f"Ошибка при добавлении книги: {e}")


def show_books(lib: Library):
    """Отображение всех книг в библиотеке."""
    print("\n--- Список книг в библиотеке ---")
    if not lib.books:
        print("Библиотека пуста.")
    else:
        for book in lib.books:
            print(f"ID: {book.id} | {book} | Страниц: {book.pages}")
            # Дополнительно можно показать repr
            # print(f"  repr: {repr(book)}")


def find_index(lib: Library):
    """Поиск индекса книги по ID."""
    print("\n--- Поиск индекса книги по ID ---")
    try:
        id_str = input("Введите ID книги: ").strip()
        if not id_str:
            print("Ошибка: ID не может быть пустым.")
            return
        search_id = int(id_str)

        index = lib.get_index_by_book_id(search_id)
        book = lib.books[index]
        print(f"Книга с ID {search_id} найдена под индексом {index}.")
        print(f"Детали: {book} (страниц: {book.pages})")
    except ValueError as e:
        print(f"Ошибка: {e}")


def remove_book(lib: Library):
    """Удаление книги по ID (опциональная функция)."""
    print("\n--- Удаление книги по ID ---")
    try:
        id_str = input("Введите ID книги для удаления: ").strip()
        if not id_str:
            print("Ошибка: ID не может быть пустым.")
            return
        remove_id = int(id_str)

        # Используем метод Library.remove_book_by_id, если он есть
        # или реализуем прямо здесь
        # Найдём индекс и удалим
        index = lib.get_index_by_book_id(remove_id)
        removed = lib.books.pop(index)
        print(f"Книга '{removed.name}' (ID {removed.id}) успешно удалена.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    menu_library()