def use_again():
    print('Посчитать еще? Введите "д"/"н": ')

    answer = input()
    if answer in 'да':
        calc()

    else:
        print('Спасибо, что использовали калькулятор.')
        exit()

def is_valid_a(a):
    if a.isdigit():
        return True
    return False

def is_valid_action(action):
    if action in '+-*/':
        return True
    return False

def is_valid_b(b):
    if b.isdigit():
        return True
    return False

def calc():

    while True:
        a = input('Введите первое значение: ')
        if not is_valid_a(a):
            print('Пожалуйста, введите корректные данные.')
            continue

        action = input('Введите знак действия (+, -, *, /): ')
        if not is_valid_action(action):
            print('Пожалуйста, введите корректные данные.')
            continue

        b = input('Введите второе значение: ')
        if not is_valid_b(b):
            print('Пожалуйста, введите корректные данные.')
            continue


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
