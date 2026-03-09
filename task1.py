import random

# ---------- Классы ----------

class Vehicle:
    """
    Базовый класс транспортного средства.
    
    Атрибуты (доступны через свойства):
        brand (str): марка.
        year (int): год выпуска.
        mileage (float): пробег в км.
    """
    def __init__(self, brand: str, year: int, mileage: float = 0.0):
        self.brand = brand          # используется сеттер
        self.year = year
        self.mileage = mileage

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Марка должна быть непустой строкой")
        self._brand = value.strip()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int) or value < 1900:
            raise ValueError("Год выпуска должен быть целым числом >= 1900")
        self._year = value

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Пробег должен быть неотрицательным числом")
        self._mileage = float(value)

    def get_info(self) -> str:
        """Возвращает общую информацию."""
        return f"{self.brand} ({self.year}), пробег: {self.mileage} км"

    def move(self, distance: float) -> None:
        """
        Увеличивает пробег на указанное расстояние.
        
        Аргументы:
            distance: неотрицательное число.
        """
        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Дистанция должна быть неотрицательным числом")
        self.mileage += distance
        print(f"{self.brand} проехал {distance} км. Пробег теперь {self.mileage} км.")

    def __str__(self) -> str:
        return f"{self.brand} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle(brand={self.brand!r}, year={self.year}, mileage={self.mileage})"


class Car(Vehicle):
    """
    Легковой автомобиль.
    Дополнительный атрибут:
        body_type (str): тип кузова.
    """
    def __init__(self, brand: str, year: int, body_type: str, mileage: float = 0.0):
        super().__init__(brand, year, mileage)
        self.body_type = body_type

    @property
    def body_type(self) -> str:
        return self._body_type

    @body_type.setter
    def body_type(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Тип кузова должен быть непустой строкой")
        self._body_type = value.strip()

    def get_info(self) -> str:
        """Расширяет информацию, добавляя тип кузова."""
        base = super().get_info()
        return f"{base}, кузов: {self.body_type}"

    def move(self, distance: float) -> None:
        """
        Перегруженный метод: имитирует расход топлива (уменьшение уровня).
        В реальности здесь была бы проверка наличия топлива.
        """
        # Сначала родительский метод (увеличивает пробег)
        super().move(distance)
        # Дополнительная имитация: "тратим топливо"
        print(f"(Расход топлива: {distance * 0.1:.2f} л)")

    def __repr__(self) -> str:
        return f"Car(brand={self.brand!r}, year={self.year}, body_type={self.body_type!r}, mileage={self.mileage})"


class Truck(Vehicle):
    """
    Грузовой автомобиль.
    Дополнительный атрибут:
        load_capacity (float): грузоподъёмность в тоннах.
    """
    def __init__(self, brand: str, year: int, load_capacity: float, mileage: float = 0.0):
        super().__init__(brand, year, mileage)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self) -> float:
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Грузоподъёмность должна быть положительным числом")
        self._load_capacity = float(value)

    def get_info(self) -> str:
        """Расширяет информацию, добавляя грузоподъёмность."""
        base = super().get_info()
        return f"{base}, грузоподъёмность: {self.load_capacity} т"

    def move(self, distance: float, current_load: float = 0.0) -> None:
        """
        Перегруженный метод: учитывает текущую загрузку.
        Если current_load превышает грузоподъёмность, движение запрещено.
        
        Аргументы:
            distance: дистанция.
            current_load: текущая загрузка в тоннах.
        """
        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Дистанция должна быть неотрицательным числом")
        if not isinstance(current_load, (int, float)) or current_load < 0:
            raise ValueError("Загрузка должна быть неотрицательным числом")
        if current_load > self.load_capacity:
            raise ValueError("Перегруз! Движение невозможно.")
        super().move(distance)
        print(f"Грузовик перевозил {current_load} т груза.")

    def __repr__(self) -> str:
        return f"Truck(brand={self.brand!r}, year={self.year}, load_capacity={self.load_capacity}, mileage={self.mileage})"


# ---------- Вспомогательные функции для меню ----------

def clear_screen():
    """Очистка экрана (для красоты)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title: str):
    """Печатает заголовок с рамкой."""
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def print_vehicle_list(vehicles):
    """Выводит нумерованный список автомобилей."""
    if not vehicles:
        print("   Список пуст.")
        return
    for i, v in enumerate(vehicles):
        prefix = "🚗" if isinstance(v, Car) else "🚛" if isinstance(v, Truck) else "🚙"
        print(f"{i+1:2}. {prefix} {v} | {v.get_info()}")

def get_int_input(prompt: str, min_val=None, max_val=None) -> int:
    """Безопасный ввод целого числа с проверкой диапазона."""
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Значение должно быть от {min_val} до {max_val}.")
                continue
            return val
        except ValueError:
            print("Ошибка: введите целое число.")

def get_float_input(prompt: str, min_val=None, max_val=None) -> float:
    """Безопасный ввод числа с плавающей точкой."""
    while True:
        try:
            val = float(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Значение должно быть от {min_val} до {max_val}.")
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

# ---------- Генерация случайных автомобилей ----------

BRANDS = ["Toyota", "Ford", "Volvo", "BMW", "Mercedes", "Scania", "MAN", "Honda", "Nissan", "Tesla"]
BODY_TYPES = ["седан", "хэтчбек", "универсал", "внедорожник", "купе", "минивэн"]

def generate_random_vehicle(vehicle_type: str = None):
    """
    Создаёт случайный автомобиль указанного типа.
    Если тип не указан, выбирается случайно.
    """
    if vehicle_type is None:
        vehicle_type = random.choice(["Car", "Truck"])
    
    brand = random.choice(BRANDS)
    year = random.randint(1990, 2025)
    mileage = round(random.uniform(0, 300000), 1)
    
    if vehicle_type == "Car":
        body_type = random.choice(BODY_TYPES)
        return Car(brand, year, body_type, mileage)
    else:  # Truck
        load_capacity = round(random.uniform(1.5, 40.0), 1)
        return Truck(brand, year, load_capacity, mileage)

def generate_multiple_vehicles(count: int):
    """Генерирует список из count случайных автомобилей."""
    return [generate_random_vehicle() for _ in range(count)]

# ---------- Подменю работы с выбранным автомобилем ----------

def vehicle_detail_menu(vehicle):
    """Меню для взаимодействия с конкретным автомобилем."""
    while True:
        clear_screen()
        print_header(f"Детальный просмотр: {vehicle}")
        print(f"Тип: {'Легковой' if isinstance(vehicle, Car) else 'Грузовой' if isinstance(vehicle, Truck) else 'Базовый'}")
        print(vehicle.get_info())
        print("\nДоступные действия:")
        print("1. Показать информацию (get_info)")
        print("2. Переместить (move)")
        print("3. Изменить параметры")
        print("4. Вернуться к списку")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            input(vehicle.get_info() + "\nНажмите Enter, чтобы продолжить...")
        
        elif choice == "2":
            try:
                if isinstance(vehicle, Truck):
                    dist = get_float_input("Введите расстояние (км): ", min_val=0)
                    load = get_float_input("Введите текущую загрузку (т): ", min_val=0)
                    vehicle.move(dist, load)
                else:
                    dist = get_float_input("Введите расстояние (км): ", min_val=0)
                    vehicle.move(dist)
            except ValueError as e:
                print(f"Ошибка: {e}")
            input("Нажмите Enter, чтобы продолжить...")
        
        elif choice == "3":
            edit_vehicle_menu(vehicle)
        
        elif choice == "4":
            break
        
        else:
            print("Неверный ввод.")
            input("Нажмите Enter...")

def edit_vehicle_menu(vehicle):
    """Меню изменения параметров автомобиля."""
    while True:
        clear_screen()
        print_header(f"Редактирование: {vehicle}")
        print("Текущие параметры:")
        print(f"  1. Марка: {vehicle.brand}")
        print(f"  2. Год: {vehicle.year}")
        print(f"  3. Пробег: {vehicle.mileage}")
        if isinstance(vehicle, Car):
            print(f"  4. Тип кузова: {vehicle.body_type}")
        elif isinstance(vehicle, Truck):
            print(f"  4. Грузоподъёмность: {vehicle.load_capacity} т")
        print("  0. Вернуться")
        
        choice = input("Выберите параметр для изменения (0-4): ").strip()
        
        if choice == "0":
            break
        try:
            if choice == "1":
                new_val = get_string_input("Новая марка: ")
                vehicle.brand = new_val
                print("Марка обновлена.")
            elif choice == "2":
                new_val = get_int_input("Новый год выпуска: ", min_val=1900, max_val=2100)
                vehicle.year = new_val
                print("Год обновлён.")
            elif choice == "3":
                new_val = get_float_input("Новый пробег: ", min_val=0)
                vehicle.mileage = new_val
                print("Пробег обновлён.")
            elif choice == "4":
                if isinstance(vehicle, Car):
                    new_val = get_string_input("Новый тип кузова: ")
                    vehicle.body_type = new_val
                    print("Тип кузова обновлён.")
                elif isinstance(vehicle, Truck):
                    new_val = get_float_input("Новая грузоподъёмность (т): ", min_val=0.1)
                    vehicle.load_capacity = new_val
                    print("Грузоподъёмность обновлена.")
                else:
                    print("У этого автомобиля нет четвёртого параметра.")
            else:
                print("Неверный выбор.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        input("Нажмите Enter...")

# ---------- Главное меню ----------

def main_menu():
    vehicles = []
    # Добавим несколько демо-автомобилей
    vehicles.append(Car("Toyota Camry", 2020, "седан", 15000))
    vehicles.append(Truck("Volvo FH", 2019, 20.5, 120000))
    vehicles.append(Car("Honda Civic", 2022, "хэтчбек", 5000))
    
    while True:
        clear_screen()
        print_header("АВТОПАРК (задание 3: наследование)")
        print("Список автомобилей:")
        print_vehicle_list(vehicles)
        print("\nМеню:")
        print("1. Добавить новый автомобиль")
        print("2. Сгенерировать случайные автомобили")
        print("3. Выбрать автомобиль для детального просмотра (по номеру)")
        print("4. Удалить автомобиль (по номеру)")
        print("5. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            add_vehicle_menu(vehicles)
        elif choice == "2":
            generate_vehicles_menu(vehicles)
        elif choice == "3":
            select_vehicle_menu(vehicles)
        elif choice == "4":
            delete_vehicle_menu(vehicles)
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод.")
            input("Нажмите Enter...")

def add_vehicle_menu(vehicles):
    """Меню добавления нового автомобиля (ручной ввод)."""
    clear_screen()
    print_header("Добавление нового автомобиля")
    print("Выберите тип:")
    print("1. Легковой (Car)")
    print("2. Грузовой (Truck)")
    type_choice = input("Ваш выбор (1/2): ").strip()
    
    try:
        brand = get_string_input("Марка: ")
        year = get_int_input("Год выпуска: ", min_val=1900, max_val=2100)
        mileage = get_float_input("Пробег (км, можно 0): ", min_val=0)
        
        if type_choice == "1":
            body_type = get_string_input("Тип кузова: ")
            vehicle = Car(brand, year, body_type, mileage)
        elif type_choice == "2":
            load_cap = get_float_input("Грузоподъёмность (т): ", min_val=0.1)
            vehicle = Truck(brand, year, load_cap, mileage)
        else:
            print("Неверный выбор типа.")
            input("Нажмите Enter...")
            return
        
        vehicles.append(vehicle)
        print(f"Автомобиль {vehicle} успешно добавлен!")
    except ValueError as e:
        print(f"Ошибка при создании: {e}")
    input("Нажмите Enter...")

def generate_vehicles_menu(vehicles):
    """Меню генерации случайных автомобилей."""
    clear_screen()
    print_header("Генерация случайных автомобилей")
    count = get_int_input("Сколько автомобилей сгенерировать? ", min_val=1, max_val=20)
    new_vehicles = generate_multiple_vehicles(count)
    vehicles.extend(new_vehicles)
    print(f"Сгенерировано {count} автомобилей.")
    input("Нажмите Enter...")

def select_vehicle_menu(vehicles):
    """Выбор автомобиля по номеру для детального просмотра."""
    if not vehicles:
        print("Список пуст. Нечего выбирать.")
        input("Нажмите Enter...")
        return
    print_vehicle_list(vehicles)
    idx = get_int_input("Введите номер автомобиля: ", min_val=1, max_val=len(vehicles)) - 1
    vehicle_detail_menu(vehicles[idx])

def delete_vehicle_menu(vehicles):
    """Удаление автомобиля по номеру."""
    if not vehicles:
        print("Список пуст. Нечего удалять.")
        input("Нажмите Enter...")
        return
    print_vehicle_list(vehicles)
    idx = get_int_input("Введите номер автомобиля для удаления: ", min_val=1, max_val=len(vehicles)) - 1
    removed = vehicles.pop(idx)
    print(f"Автомобиль {removed} удалён.")
    input("Нажмите Enter...")

if __name__ == "__main__":
    main_menu()