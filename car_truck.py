# Создать 1 экземпляр класса Наследника
# Создать класс наследник - Грузовик. Который, наследует все атрибуты класса, но количество колес = 8.
# Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description)

from car_main import *

#наследование от car

class CarTruck(Car):
    def __init__(self, model, year, engine, price, mileage, wheels):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(model, year, engine, price, mileage, wheels)
        self.wheels = 8

    def description_car(self):
        """Переопределение метода родителя"""
        description = (f'Машина называется {self.model}, произведена в {self.year}. '
                       f'Мотор {self.engine}. Стоимость - {self.price}. Пробег - {self.mileage}. Количество колес - {self.wheels}.')
        print(f'{description}')

truck = CarTruck('Nissan Atlas', 2023, 150, 8000000, 200000, 8)
truck.description_car()