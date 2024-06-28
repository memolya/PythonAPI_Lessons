def use_again():
    print('Посчитать еще? Введите "д"/"н": ')

    answer = input()
    if answer in 'да':
        calc()

    else:
        print('Спасибо, что использовали калькулятор.')
        exit()

def is_valid(a, action, b):
    if a.isdigit() and b.isdigit() and action in '+-*/':
        return True
    return False

def calc():

    while True:
        a = input('Введите первое значение: ')
        action = input('Введите знак действия (+, -, *, /): ')
        b = input('Введите второе значение: ')

        if not is_valid(a, action, b):
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
