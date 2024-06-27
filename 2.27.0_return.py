# def identification(name):
#     print('Вы являетесь ', end = '')
#     if name == 'Alex':
#         print('автором')
#     else:
#         print('студентом')
#
# name = input('Ввдите ваше имя: ')
# identification(name)

def identification(name):
    print('Вы являетесь ', end = '')
    if name == 'Alex':
        result = 'автором'

    else:
        result = 'студентом'

    return result

def status(result):
    print(result)

name = input('Введите ваше имя: ')
result = 5
#function (identification) indside another (status) function
status(identification(name))

# print(identification(name))
# n = 'Alex '
# s = identification(name)
# print(n + s)