#
# Task #1
a = 10
for i in range (1,21):
    print(a)

# Task #2
a= int(input ("Введите  начало :"))
b= int(input ("Введите  конец :"))
for i in range (a,b ) :
    a+=1
    print( a )
#
# Task #8
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)

#
# Task #6
s = 0
for i in range(100, 501):
    s += i
    print(s, end=" ")

#
# Task #7
for i in range (5,20 ) :
    print(i **2)

#
# Task 3
N=int(input())
for i in range(1,N):
    print ( i **2)

#
# Task # 4
for i in range(100 ,-101,-1) :
    print(i , end= " " )

#
# Task 9
s= input(" Введите текст :")
for i in range (len(s)):
     if s [i]== "с" :
         print(i,s [i])

#
# Task # 11

l = input()
for i in range (len (l)):
    if int(i) % 2 == 0:
        print(i)

#
# Task 14

f1 = f2 = 1

n = int(input())

print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
#
# Task # 13

n = int(input( " На лугу  "))
if n in range(11, 15):
        print(n, 'коров',end= "")
else:
        t = n % 10
        if t in list(range(5,10))+[0]:
                print(n, 'коров ',end= "" )
        if t == 1:
                print(n, 'корова',end= "")
        if t in range(2,5):
                print(n, 'коровы',end= "")


#
# Task # 10
s= input("Введите строку :")
s1 = ""
for i in s :
    if i not in s1:
        s1 += i
        print( s1)

 #Task 13

n= int(input())
for i in range (1, n+1) :
    if i%10== 1 and i%100!=11 :
        print(f "на лугу {i} корова ")