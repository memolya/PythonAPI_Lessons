# def description(name, age, gender):
#     print(f"Имя {name}, Возраст {age}, Пол {gender}")

#positional argument
# description('Alex', 30, 'man')

#named arg
# description(age = 30, gender = 'man', name ='Alex')

n = 'Anna'
a = 30
def description(name, age, gender):
    print(f"Имя {name}, Возраст {age}, Пол {gender}")

description(n, a, 'woman')