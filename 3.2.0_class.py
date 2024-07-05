class Person():
    #""" - используем когда нам нужно сделать аннотацию, чтоб это было сразу видно посередине экрана, скажем так чего-то важного. В нем не может быть рабочего кода, а # - это коммент, сбоку, пояснение для чего-то, это может быть частью кода
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        #вес человека по умолчанию - будет применяться ко всем экземплярам класса
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        #f-string notation позволяет передавать int в конкатенацию строки без изменения типа данных на str
        description = f'Этого человека зовут {self.name}, ему {self.age} лет, его рост {self.height}, его вес {self.weight}'
        print(f'{description}')

    def get_weight(self):
        """Получение веса человека"""
        print(f'Вес этого человека: {self.weight}')

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

man = Person('Alex', 30, 180)
# man.description_person()

#редактирование веса для экземпляра класса man без объявления нового метода
# man.weight = 110

man.update_weight(110)
man.get_weight()