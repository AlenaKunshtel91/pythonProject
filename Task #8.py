# #
# # Task #1
# a=input().split()
# for elem in a :
#     if int(elem) % 2==0 :
#         print(elem)
#
# #
# # Task #2
# list= [3, 2, 8, 5, 11, 6]
# list2 = [2, 7, 9, 3, 20, 4]
# c=[]
# for i in list :
#         if i not in list2:
#          c.append( i)
# if c ==[]:
#     print("не найдено:")
# else:
# print(min(c))
#
# #
# # Task # 4
# list = ["ха","ха","ха","ха"]
# delimiter="-"
# s= delimiter.join((list))
# for i in list :
#     if list.count(i)>3:
#          list.remove(i)
#          print(s[0:4:1])
#
#
# #Task #3
# import random
# g=0
# lst=[]
# count=0
# n=int(input('введите количество элементов в списке'))
# for i in range (0,n):
#       l = random.randint(0, 100)
# lst.insert(i,l)
# if n>=i>0:
#    if g>l:
#       count += 1
#       g=l
# print(lst)
# print(count)
#
#  # Task 8
# list = [100, 75, 100, 20, 75, 12, 75, 25]
# s = []
# for i in list:
#     if i not in s:
#         s.append(i)
# print("неповторяющие элементы:\n",i)
#
# # Task 5
# import random
# list=[]
# el=''
# n=int(input('введите кол-во элем-тов:'))
# for i in range (0,n):
#     m=random.randint(0,1000)
#     print('m',m)
#     list.insert(n+n,m)
#     if m%2==0:
#         m=str(m)
#         el=int(m[::-1])
#         list.insert(n+n,el)
#     print('Список четных чисел:',list)


#
# Task # 10
lst = []
s = input("enter srting:")
while s != ".":
    s = s.split(maxsplit=1)
    if (len(s)) == 2:
        lst.append(s[1])
    elif s[0]== "GET":
        print(lst[-1])
    elif s[0]== "DELETE" :
        del lst[-1]
    s = input("enter srting:")
print(lst)


a = input().split()
print(sum(a.count(x) - 1 for x in a) // 2)