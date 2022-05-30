# # number=1
# while number <=10:
#     print(number)
#     number +=1

# #number=11
# while number >=10:
#     print(number)
#     number -=1

# #number = 100
# while number <= 999:
#     s = number // 100 + number % 100 + number // 10 % 10
#     if s == 10:
#         print(number, end="")
#         number += 1

# Task #1
n = int(input(" число :"))
number = 1
while number <= n:
    print(number)
    number += 1

# Task #2
n = int(input(" число :"))
s = 0
i= 0
while i <= n :
    i+=1
    if  i % 2==0 :
        s+=i
print(s)
