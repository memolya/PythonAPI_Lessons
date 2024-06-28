a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print('На 0 делить нельзя')

print('Частное: ' + str(result))

result_2 = a + b
print('Сумма: ' + str(result_2))

#zero division error