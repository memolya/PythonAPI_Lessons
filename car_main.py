# Создайте класс Car. Добавьте обязательные атрибуты класса: модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4.
# Создайте 1 экземпляр класса
# Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description)

class Car():
    """Создаем машину"""
    def __init__(self, model, year, engine, price, mileage, wheels):
        """Инициализируем атрибуты машины"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        #default wheels
        self.wheels = 4

    def description_car(self):
        """Возврат информации об автомобиле"""
        description = (f'Машина называется {self.model}, произведена в {self.year}. '
                       f'Мотор {self.engine}. Стоимость - {self.price}. Пробег - {self.mileage}. Количество колес - {self.wheels}.')
        print(f'{description}')

# car = Car('Juke', 2010, 100, 1500000, 75000, 4)
# car.description_car()
