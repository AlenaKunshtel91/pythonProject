# #
# for i in range (1,4):
#      for j in range (1,i+1):
#       print(i, end= " ")
#      print()

# #
# number=int(input("Введите число :"))
# count =0
# for i in range (1, number +1):
#     if number% i==0 :
#         count+=1
#
# if count ==2:
#     print("простое" )
# else:
#     print("составное")

# #
# # Ввывести все простые числа от 2 до 100
#
# for j in range(2,100):
#   count =0
#   for i in range (1, j +1):
#     if j% i==0 :
#         count+=1
#         break
#     if count ==0:
#      print(j,end= " ")

# #
# # Ввывести все простые числа от 2 до 100 с циклом while
# j=2
# while j<=100:
#    count =0
#    for i in range (2, j// 2+1):
#       if j% i==0 :
#         count+=1
#         break
#       if count ==0:
#        print(j,end= " ")
#    j+=1

# #
# n= int(input())
# for i in range (1, n+1) :
#     if i%10== 1 and i%100!=11 :
#         print( f"на лугу {i} корова ")
#     elif i%10==2 and i%100 !=12 or i %10==3 and i %100 !==13 or i%10==4 and i%100!=14 :
#     print (f"на лугу {i} коровы")
# else:
#     print(f"на лугу {i} коровы")

# #
# s="Привет я ваша тетя"
# s+= " "
# s1=" "
# for elem in s :
#   if elem != " " :
#     s1+= elem
#   elif s1 :
#     print(s1)
#     s1= " "



for i in range(1, n + 1):
  if i ** 2 <= n:
   print(i ** 2, end=' ')