# 1.Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке
# a=set(input())
# b=-1
# for i in a:
#     b+=1
#     print(b)
# 2. список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
#
# a=[1,1,2,2,3,3,1]
# print(sum((a.count(x) // 2 for x in (x for x in set(a) if a.count(x) > 1))))
#
# # 6.Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# set = {1, 2, 3, 4, 5, 6, 6, 7}
# set2 = {2, 9, 8, 7, 6, 5, 4, 5}
# output = set & set2
# print(len(output))
#
# 3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2)Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей
#
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# print(C_1 if sum(C_1) > sum(C_2) else C_2)
# print("Max element:",max(C_2),"Min element:",min (C_2))
# print("Min element:",min(C_1),"Max element:",max(C_1))
#
# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.
# word = " An apple a day keeps the doctor away"
# dict = {symb: word.count(symb) for symb in word}
# print(dict)
#
# 7.Напишите программу, демонстрирующую работу try\except\finally
# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)
# finally:
#     print("Молодец")

# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу
# #
f = open("class.txt",encoding="utf-8")
sum = 0
n = 0
for s in f:
    s = s.split()
    d = int(s[2])
    sum +=  d
    n += 1
    if d < 4:
        print(s[0], s[1] , s[2])
f.close()
print('Средний балл %.2f' %(sum/n))