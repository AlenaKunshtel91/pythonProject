# 1.Напишите функцию m(a, b), вычисляющую минимум двух чисел.
# a=int(input())
# b=int(input())
# def min2(a,b):
#     m=min(a,b)
#     return m
# print(min2(a, b))
#
# 2.Найдите минимальное четырёх чисел с помощью функции написанной в предыдущей  задаче. Новую функцию не создавать! Использовать функцию из предыдущей задачи!
# a=int(input())
# b=int(input())
# c=int(input())
# f=int(input())
# def min4(a,b ,c ,f):
#     m=min(a,b,c,f)
#     return m
# print(min4(a, b,c,f))
#
# 4.	Дано натуральное число n > 1. Проверьте, является ли оно простым. Программа должна вывести слово YES, если число простое и NO, если число составное.
# def natur(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n
# x = int(input())
# if natur(x) == True:
#     print('YES')
# else:
#     print('NO')
#
# 5.Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# def fin(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n == 3:
#         return 2
#     else:
#         return fin(n - 1) + fin(n -2)
# print(fin(int(input())))
#
# 7.Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка.
# def modify_list(l):
#     for i in reversed(range(len(l))):
#         if l[i] % 2 == 0:
#             l[i] = l[i] // 2
#         else:
#             del l[i]
# l = [int(i) for i in input().split()]
# modify_list(l)
# print(l)


#3.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа и выведите результат работы этой функции.
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# def distance(x1, y1, x2, y2):
#     return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)
# print (distance(x1, y1, x2, y2))


