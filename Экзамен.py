# #
# # 2
# s = input("Ввести строку :")
# gls = 0
# sgl = 0
# vse_gls = ("y", "u", "a", "e", "o", "i")
# for i in s:
#     if i in vse_gls:
#         gls += 1
#     else:
#         sgl += 1
# print(f"количество гласных: ", { gls} , "количество соглачных :", {sgl})
# if gls==sgl:
#     print(gls)
# #
# # 1
# n = int(input("Ввести число :"))
# c = 0
# d = 0
# s = 0
# for x in range(0, 8):
#     if not x % 2:
#         c += 1
# else:
#     d += 1
# print("Четные числа  :", c)
# print("Нечетные числа :", d)
# if c > d:
#  for i in range(1, 8):
#   s+=n % 10
#   c += 1
# n = n // 10
# print("сумма =" ,s)
#
# #
# # Task # 4
# import random
# a= int(input('введите кол-во проверок'))
# b= int(input('введите искомую цифру'))
# for i in range(0,a):
#  c = random.randint(1, 101)
# s=str(a)
# d=str(b)
# if d in s:
#         print(s.count(d))

# # 6
# s = input("Ввести строку :")
# gls = 0
# sgl = 0
# c=0
# count=0
# upper=0  #верхний
# lower=0  #нижний
# vse_gls = ("y", "u", "a", "e", "o", "i")
# for i in s:
#     if i in vse_gls:
#         gls += 1
#     else:
#         sgl += 1
# print(f"количество гласных: ", { gls} , "количество соглачных :", {sgl})
# for i in s:
#           c+=1
# print("количество букв =",+c)
# for i in s:
#       if i.islower() :
#          lower+=1
#       elif  i.isupper():
#          upper+=1
# print("Количество в нижнем регистре:")
# print(upper)
# print("Количество в ввернем регистре:")
# print(lower)


list=[24,12,46,3,7,48]
k=str(k)
for i in list:
    if i%2==0 :
       i.reverse(k)
print(i)

