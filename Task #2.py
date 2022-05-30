
 # Task #3
 n = int(input(" Введите число :"))
 k = int(input("Введите число : "))
 if n % 2 == 0 and k % 2 == 0:
     print("числа имеют одинаковую четность ")
 else:
     print(" число имеют неодинаковую четность ")

 # Task #4
x = int(input(" Введите число :"))
a = int(input(" Введите число :"))
 c = int(input(" Введите число :"))
 print(x % 3 == 0 and x % 3 == 0)
 print(a % 3 == 0 and a % 3 == 0)
 print(c % 3 == 0 and c % 3 == 0)

# Task #5

a, b, c = map(int, input("Введите число : " ).split())
x = 0
if a % 2 == 0:
     x = x + 1
if b % 2 == 0:
     x = x + 1
if c % 2 == 0:
     x = x + 1
print(x)



# Task #7
a = int(input("Ввведи год :"))
if a % 4 == 0  and not a % 100 == 0 or a % 100 == 0 :
    print("Yes")
else:
    print("Not")

# Task #8
a = bool(int(input("0/1 : ")))
b = bool(int(input("0/1 : ")))
c = bool(int(input("0/1 : ")))
print(a, b, c)
T = a and not (b and not c)
S = a and not b or a and c
print(T)
print(S)
print(T == S)
