# 1. Реализуйте класс SquareFunction, экземпляры которого при
# инициализации получают коэффициенты a, b, c. При вызове
# объекта как функции с аргументом x должно возвращаться
# значение выражения a*x**2 + b*x + c.
# class SquareFunction:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __call__(self, x):
#         return self.a * x ** 2 + self.b * x + self.c
# sf = SquareFunction(1, 2, 5)
# print(sf(4))

#  5.Создайте класс Students. Реализуйте добавление нового имени,
# возраста а также среднего бала студента. Создайте несколько
# студентов, а затем выведите старшего студента и студента с
# самым высоким баллом
# class Students(object):
#
#     def __init__(self, name):
#         self.group_students = []
#         self.filename = f'{name}.txt'
#
#     def add_students(self, data):
#         with open(self.filename, 'a') as datafile:
#             datafile.write(data + '\n')
#         self.group_students.append(data.split())
#
#     def info(self, number):
#         number -= 1
#         if len(self.group_students) < number < 0:
#             print('Нет такого номера в списке')
#         else:
#             print(*self.group_students[number])
#
#     def selec(self, age):
#         for data in self.group_students:
#             if data[-1] == age:
#                 print(*data)
#
#     def fileinfo(self):
#         with open(self.filename) as f:
#             print(*f.read().split('\n'), sep='\n')
#
#
# stud = Students(input('введите имя файла для записи ->  '))
# print('''выберите действие.
#                 1 - добавить студента, 2 - вывод по номеру
#                 3 - вывод по возрасту, 4 - вывод из файла
#                 для выхода - 0\n''')
#
# while True:
#
#     f = input('Ввод действия:  ')
#     if f == '1':
#         print('Введите данные через пробел (имя,фамилия,возраст)')
#         stud.add_students(input())
#     elif f == '2':
#         stud.info(int(input('Номер ->  ')))
#     elif f == '3':
#         stud.selec(input('Возраст-> '))
#     elif f == '4':
#         stud.fileinfo()
#     else:
#         break