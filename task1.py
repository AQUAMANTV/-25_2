class Vehicle:
    """
    Класс, представляющий транспортное средство.

    Атрибуты:
        brand (str): марка транспортного средства.
        speed (float): текущая скорость (км/ч).
        fuel_level (float): уровень топлива (литры), от 0 до 100.
    """

    def __init__(self, brand: str, speed: float, fuel_level: float) -> None:
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Марка должна быть непустой строкой")
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Скорость должна быть неотрицательным числом")
        if not isinstance(fuel_level, (int, float)) or not (0 <= fuel_level <= 100):
            raise ValueError("Уровень топлива должен быть числом от 0 до 100")
        self.brand = brand
        self.speed = speed
        self.fuel_level = fuel_level

    def start_engine(self) -> None:
        """Запускает двигатель."""
        pass

    def accelerate(self, amount: float) -> None:
        """Увеличивает скорость на указанную величину."""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Ускорение должно быть неотрицательным числом")
        # Здесь могла бы быть реализация
        pass

    def stop_engine(self) -> None:
        """Останавливает двигатель."""
        pass


class Furniture:
    """
    Класс, представляющий предмет мебели.

    Атрибуты:
        material (str): материал изготовления.
        color (str): цвет.
        price (float): цена в рублях (положительное число).
    """

    def __init__(self, material: str, color: str, price: float) -> None:
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Материал должен быть непустой строкой")
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Цвет должен быть непустой строкой")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.material = material
        self.color = color
        self.price = price

    def assemble(self) -> None:
        """Собирает предмет мебели."""
        pass

    def move(self, new_location: str) -> None:
        """Перемещает мебель в новое место."""
        if not isinstance(new_location, str) or not new_location.strip():
            raise ValueError("Локация должна быть непустой строкой")
        pass

    def clean(self) -> None:
        """Очищает мебель."""
        pass


class SocialMediaPlatform:
    """
    Класс, представляющий платформу социальной сети.

    Атрибуты:
        name (str): название платформы.
        users_count (int): количество зарегистрированных пользователей (>=0).
        is_active (bool): активна ли платформа в данный момент.
    """

    def __init__(self, name: str, users_count: int, is_active: bool) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(users_count, int) or users_count < 0:
            raise ValueError("Количество пользователей должно быть целым неотрицательным числом")
        if not isinstance(is_active, bool):
            raise ValueError("Флаг активности должен быть булевым значением")
        self.name = name
        self.users_count = users_count
        self.is_active = is_active

    def post_message(self, user: str, text: str) -> None:
        """Публикует сообщение от имени пользователя."""
        if not isinstance(user, str) or not user.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Текст сообщения не может быть пустым")
        pass

    def delete_user(self, user_id: int) -> None:
        """Удаляет пользователя по идентификатору."""
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("ID пользователя должен быть положительным целым числом")
        pass

    def get_trending_topics(self) -> list[str]:
        """Возвращает список актуальных тем."""
        return []


# ---------- Единое контекстное меню ----------

def main_menu():
    """Главное меню выбора объекта."""
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ: выберите объект для взаимодействия")
        print("1. Транспортное средство (Vehicle)")
        print("2. Предмет мебели (Furniture)")
        print("3. Социальная сеть (SocialMediaPlatform)")
        print("4. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            vehicle_menu()
        elif choice == "2":
            furniture_menu()
        elif choice == "3":
            social_menu()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1-4.")


def vehicle_menu():
    """Меню для работы с объектом Vehicle."""
    # Создаём экземпляр с разумными значениями по умолчанию
    try:
        v = Vehicle("Tesla", 0.0, 50.0)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return

    while True:
        print("\n--- Транспортное средство ---")
        print(f"Текущее состояние: {v.brand}, скорость={v.speed}, топливо={v.fuel_level}")
        print("1. Запустить двигатель")
        print("2. Ускориться")
        print("3. Остановить двигатель")
        print("4. Вернуться в главное меню")
        sub = input("Выберите действие: ")

        if sub == "1":
            v.start_engine()
            print("Двигатель запущен.")
        elif sub == "2":
            try:
                amount = float(input("Введите величину ускорения (км/ч): "))
                v.accelerate(amount)
                print(f"Ускорение на {amount} км/ч выполнено.")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
        elif sub == "3":
            v.stop_engine()
            print("Двигатель остановлен.")
        elif sub == "4":
            break
        else:
            print("Неверный ввод.")


def furniture_menu():
    """Меню для работы с объектом Furniture."""
    try:
        f = Furniture("дерево", "коричневый", 15000.0)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return

    while True:
        print("\n--- Предмет мебели ---")
        print(f"Текущее состояние: материал={f.material}, цвет={f.color}, цена={f.price}")
        print("1. Собрать")
        print("2. Переместить")
        print("3. Очистить")
        print("4. Вернуться в главное меню")
        sub = input("Выберите действие: ")

        if sub == "1":
            f.assemble()
            print("Мебель собрана.")
        elif sub == "2":
            try:
                loc = input("Введите новое местоположение: ")
                f.move(loc)
                print(f"Мебель перемещена в {loc}.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif sub == "3":
            f.clean()
            print("Мебель очищена.")
        elif sub == "4":
            break
        else:
            print("Неверный ввод.")


def social_menu():
    """Меню для работы с объектом SocialMediaPlatform."""
    try:
        s = SocialMediaPlatform("ExampleGram", 1000, True)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return

    while True:
        print("\n--- Социальная сеть ---")
        print(f"Платформа: {s.name}, пользователей: {s.users_count}, активна: {s.is_active}")
        print("1. Опубликовать сообщение")
        print("2. Удалить пользователя")
        print("3. Показать тренды")
        print("4. Вернуться в главное меню")
        sub = input("Выберите действие: ")

        if sub == "1":
            try:
                user = input("Имя пользователя: ")
                text = input("Текст сообщения: ")
                s.post_message(user, text)
                print("Сообщение опубликовано.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif sub == "2":
            try:
                uid = int(input("ID пользователя для удаления: "))
                s.delete_user(uid)
                print(f"Пользователь с ID {uid} удалён.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif sub == "3":
            topics = s.get_trending_topics()
            if topics:
                print("Тренды:", ", ".join(topics))
            else:
                print("Список трендов пуст (метод не реализован).")
        elif sub == "4":
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main_menu()