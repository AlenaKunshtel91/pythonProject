#
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

#
 # Task # 5
a=int(input("Ввести число :"))
for i in range (1, a+1):
    if i*i > a :
        print(i*i ,end= " ")
        break

#
# Task # 6
n = int(input(" число :"))
while n >=10:
  n = n // 10
print(n)

#
# Task #3
n = int(input("enter number: "))
s = 1
while n != 0:
    if n % 2 == 0:
        s *= n % 10
    n = n // 10
print(s)


#
# Task # 7
n= int(input( "Ввести число :"))
s =0
while n:
        s += n % 10
        n //= 10
print (s)



# Task # 4
a=int(input("Ввести число :"))
for i in range (1, a+1):
    if i**2 <=a :
        print(i**2, end=" ")