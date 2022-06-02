""
# # Task # 1
# print(17 / 2 * 3 + 2)
# print(2 + 17 / 2 * 3)
# print(19 % 4 + 15 / 2 * 3)
# print((15 + 6) - 10 * 4)
# print(17 / 2 % 2 * 3 ** 3)
# ""
#
# ""
# # Task  # 2
# print(17 / 2 * 3 + 2)
# print((2 + 17) / 2 * 3)
# print(19 % (4 + 15) / 2 * 3)
# print((15 * 4) - (10 + 6))
# print(17 / 2 % (2 * 3) ** 3)
# ""
#
# ""
# # Task # 3
# a = 1.5
# b = 3
# с = 11
# print(" Сумма = ", с - (a * b))
# ""

# #
# ""
# # Task #4
# a = 2
# b = 5
# print("Анна = " , a ,"Пол = " , b )
# ""
# #

# #
# ""
# # Task# 5
# a = int(input(" введите длину ребра "))
# print("объем равен " + str(a ** 3))
# print("площадьбоковой поверхности " + str(a * a * 4))
# ""
# #
#

# a = 2
# b = a + 2
# a += 2
# ""
# ""
# s = input("введите число")
# print(s
# a = int(input(" ведите первое целое число :"))
# b = int(input(" Введите второе целое число : "))
# c = input("Введите строку :")
# d = float(input("Введите дробное число : "))
# f = a + b + d
# print( c )
# print(f)
# # ""
# ""
# a, b, c = map(int, input("Введите число :").split())
# print(a, b, c)
# print(" Сумма = ", a + c * c)
# ""
# ""
# number = int(input("Ввести число :"))
# a = number // 100
# b = number % 100 // 10
# c = number % 10
# print(a, b, c)
# number2 = c * 100 + b * 10 + a
# print( pr
# ""
# number = input()
# if int(number) > 0:
#     print("число положительное")
#     if number > 10:
#         print("число", number, "больше 10")
# elif int(number) == 0:
#     print("число от 1 до 10 ")
# else:
#     print("число отрицательное")
#

a=[1,1,2,2,3,3,1]
print(sum((a.count(x) // 2 for x in (x for x in set(a) if a.count(x) > 1))))