from base_person import Person

#наследование от Person
class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        #супер-класс - родительский. Связать родительский класс и потомка. Связываем с методом init родителя. Дефолтный вес 100 унаследуется
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Заряд ярости"""
        print(f'Заряд ярости равен: {self.rage}')

    def description_person(self):
        """Переопределение метода родителя"""
        #f-string notation позволяет передавать int в конкатенацию строки без изменения типа данных на str
        description = f'Этого человека зовут {self.name}, ему {self.age} лет, его заряд ярости {self.rage}'
        print(f'{description}')

war = Warrior('Fjfj', 30, 200)
war.description_person()