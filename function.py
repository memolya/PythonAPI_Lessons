# # num_1 = 10
# # num_2 = 20
# # # result = num_1 + num_2
# # # print(result)
# # #
# # # num_1 = 30
# # # num_2 = 40
# # # result = num_1 + num_2
# # # print(result)
#
# def sum(num_1, num_2): #2 args - 10 and 20 or 30 and 40
#     result = num_1 + num_2
#     print(result)
#
# sum(10, 20)

name, age = 'Alex', '32'
def hi(name, age):
    result = name + ' ' + age
    #print(result)
    return result

h = hi(name, age)
#hi(name, age)
print(h)