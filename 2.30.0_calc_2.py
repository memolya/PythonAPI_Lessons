def use_again():
    print('Посчитать еще? Введите "д"/"н": ')

    answer = input()
    if answer == 'да':
        calc()

    else:
        print('Спасибо, что использовали калькулятор.')
        exit()

def is_valid_a(a):
    if a.isdigit():
        return True
    return False

def is_valid_action(action):
    if action == '+' or action == '-' or action == '*' or action == '/':
        return True
    return False

def is_valid_b(b):
    if b.isdigit():
        return True
    return False

def calc():
    a = input('Введите первое значение: ')
    while is_valid_a(a) == False:
        print('Пожалуйста, введите корректные данные.')
        a = input('Введите первое значение: ')
        continue

    action = input('Введите знак действия (+, -, *, /): ')
    while is_valid_action(action) == False:
        print('Пожалуйста, введите корректные данные.')
        action = input('Введите знак действия (+, -, *, /): ')
        continue

    b = input('Введите второе значение: ')
    while is_valid_b(b) == False:
        print('Пожалуйста, введите корректные данные.')
        b = input('Введите второе значение: ')
        continue

    while True:

        if action == '+':
            result = int(a) + int(b)
            print('Сумма: ' + str(result))
        elif action == '-':
            result = int(a) - int(b)
            print('Разница: ' + str(result))
        elif action == '*':
            result = int(a) * int(b)
            print('Произведение: ' + str(result))
        else:
            try:
                result = int(a)/int(b)
                result = round(result, 2)
            except ZeroDivisionError:
                result = 0
                print('На 0 делить нельзя')

            print('Частное: ' + str(result))
        use_again()

calc()
