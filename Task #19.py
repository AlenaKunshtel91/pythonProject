# 4.Напишите рекурсивную функцию get_length(obj), которая принимает на вход
# итерируемый объект (строку, список или кортеж) и выводит его длину.
# Функцию len для выхода из рекурсии не используем
# def get_length(lst):
#     if not lst:
#         return 0
#     return 1 + get_length(lst[1:])
# a = [1,4,5,4,3,2,3]
# print("Длина списка равна: ")
# print(get_length(a))


# 5.Напишите рекурсивную функцию digits(n), которая принимает натуральное
# число и возвращает строку с цифрами этого числа справа налево, разделяя их
# пробелами.
# def func(x):
#     if x != 0:
#         print(x % 10, end=' ')
#         func(int(x / 10))
# func(14623)

# 6.Напишите рекурсивную функцию is_power(n), которая возвращает True, если
# переданное натуральное число является степенью двойки, и False иначе.
# def is_power(n):
#     n = n/2
#     if n == 2:
#         return True
#     elif n > 2:
#        return is_power(n)
#     else:
#         return False
# if is_power(1048576):
#     print ('True')
# else:
#     print ( 'False')


# 10.Дано натуральное число N. Вычислите сумму его цифр
# l = []
# def sum_digits(b):
#     if (b == 0):
#         return l
#     dig = b % 10
#     l.append(dig)
#     sum_digits(b // 10)
# n = int(input("Введите число: "))
# sum_digits(n)
# print(sum(l))


# class Human:
#     # name = "Vasya"
#     # age = 25
#     def set_name(self, name) :
#         self.name=name #динамическое свойства
#     def set_age(self,age):
#         self.age=  age
#         def info(self):
#             print(f"name{self.name}age{ self.age}")
# Vasya = Human()
# Men = Human()
# Men.set_name("Katya")
# Men.set_age(28)
# Men2 = Human()
# Men2.set_name("Vasya")
# Men2.set_age(25)
# Men.info()
# Men2.info()
# if Men.age>Men2.age:
#     print(f"{Men.name}older")
# print(Men.name)
# print(Human.set_name())


# class Human:
#     def __init__(self,age ,name,weght):
#         self.name= name
#         self.age= age
#         self.weight=weght
#
#     def set_name(self, name) :
#         self.name= name
#
#     def set_age(self,age):
#         self.age=  age
#
#     def set_weght(self, weght):
#         self.weght = weght
#
#     def info(self):
#         print(f"name{self.name}age{ self.age} weght {self.weght}")
#
# Vasya =Human("Vasya", 29,65)
# Vasya.info()
# print("after year :")
# Vasya.set_weght(54)
# Vasya.set_age(29)
# Vasya.info()

# class fraction:
#     def __init__(self,a,b):
#         self.a= a
#         self.b=b
#
#     def info(self):
#         print(f"{self.a}/{self.b}")
#
#     def kratko(self):
#         a=self.a
#         b=self.b
#         while a!=0 and b!=0 :
#             if a>b:
#                 a%=b
#             else:
#                 b%=a
#         self.nod= a+b
#         if self.nod !=1:
#             self.a//=self.nod
#             self .b//=self.nod
#             self.info()
#         else:
#             print("сократить дробь не возможно")
#             self.info()
#
#
# frac1 = fraction(3, 5)
# frac1.info()
# frac1.kratko()

################################################ Урок ООП №2
# class Human :
#     def __init__(self, name ,age):
#         self.name= name
#         self.age = age
#
#     # методы экземплера класса
#     def info(self):
#         print(self.name,self.age)
#
#     # статический метод
#
#     @staticmethod
#     def weather(temp):
#         print("weather is cloudy")
#         if temp>=25:
#             print("it very hot")
#         else:
#             print("it normaly")
#     # елассовый метод
#     @classmethod
#     def person_create(cls, name):
#         return cls (name,54)
#
#
# Vasya=Human("Vasya",24)
# Vasya.info()
# Human.info(Vasya)
# Vasya.weather(67)
# Human.weather(-23)
# Kolya = Human.person_create("Kolya")
# Kolya.info()
# Vasya= Vasya.person_create("Petya")
# Vasya.info()


#инкапсуляция ООП
# class Human :
#     name = "Vasya" #public
#     _age= 25 # protected
#     __weight= 90.24 # private
#
#
#     @staticmethod
#     def info():
#         print(Human.name,Human._age,Human.__weight)
#
#
#     def info1(self):
#         Human.__info()
#
# Vasya= Human()
# print(Vasya.name)
# print(Vasya._age)
# print(Vasya._Human__weight)
# Vasya._Human__info()
# Vasya.info1()


########Наследование
# Множестевенное наследование
class Car():
    def set_model (self,model):
        self.model=model
class Human (object):
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def info(self):
        print(self.name,self.age)

class Car():
    def __init__(self,model):
     def set_model (self,model):
        self.model=model

    def info(self):
        Car.info(self)
        print(self.model)

class Drive (Car,Human):
    def __init__(self,name,age, model):
        super().__init__(name,age)
        Car.__init__(self,model)

    def year_of_drive(self,year):
        self.year=year

    def info_driver(self):
        print(self.year)
        self.info()
        Car.info(self)

Vasya= Drive("Vasya",25,"Volvo",5)
# Vasya.set_model('Volvo')
# Vasya.info()
# Car.info(Vasya)
Vasya.info_driver()