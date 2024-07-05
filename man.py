#from base_person import Person, Warrior
#можем создавать экземпляры классов Person и Warrior в этом файле

# from base_person import *
# import * - импортировать все классы из модуля base_person

import base_person as bp

man = bp.Person('Alex', 30, 180)
man.description_person()

warrior = bp.Warrior('Konan', 32, 200)
print('Этого воина зовут: ' + warrior.description_person())

# Персонаж (Родительский класс)

# подкласс: Раса (люди, эльфы, гномы, орки)
# подкласс: Специальность (воин, маг, лучник)

# Родительский класс                        Персонаж

# Подкласс                      Раса                    Специальность

# Подкласс подкласса    люди эльфы гномы орки         воин    маг   лучник