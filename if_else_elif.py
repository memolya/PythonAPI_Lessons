pin = 1234
print('Введите пин-код')
user_pin = int(input())

if pin == user_pin:
    print('Какую сумму вы хотите снять?')
else:
    print('Ошибка. Введите корректный пин-код. Осталось 2 попытки.')
    user_pin = int(input())
    if pin == user_pin:
        print('Какую сумму вы хотите снять?')
    else:
        print('Ошибка. Введите корректный пин-код. Осталось 1 попытка.')
        user_pin = int(input())
        if pin == user_pin:
            print('Какую сумму вы хотите снять?')
        else:
            print('Ошибка. Ваша карта заблокирована. Обратитесь в банк.')

