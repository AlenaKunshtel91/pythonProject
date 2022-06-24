
# Task 3
for i in range (5,0,-1):
    for j in range (1,i+1):
     print(i, end=" ")
    print()


# Task 4
number =int(input("Ввести число:"))
a=number//100
b=number%100//10
c=number %10
number1=a+b+c
print(number1)

# Task #1
n = int(input("Ввести число :"))
for i in range(1, 10):
    print(f" {n} * {i} ={ n * i } ")

# Task  #9
s = input('Введите текст: ')
for i in s:
    s = s.replace(',', ', ')
    s = s.replace('  ', ' ')
    s = s.replace(',  ', ', ')
print(s)

#Task #2
n=1
for i in range (1,11) :
     if n!=0 :
      print(random.random())


#Task # 5
n=int(input("enter number :"))
for i in range(1, n + 1):
   print(i, * ['+' * (i % j == 0 ) for j in range(1, i + 1)], sep="" )


Task  # 6
a, b = map(int, input().split())
ls = []
for i in range(a, b + 1):
    if all(i % n != 0 for n in range(2, i)):
       ls.append(str(i))
if len(ls):
    print(' '.join(ls))
else:
    print(0, end = " ")




