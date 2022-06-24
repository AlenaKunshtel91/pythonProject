#  Классная работа
# Task #1
lst=[0,1,2,3,4,5,6,7,8,9]
tup=tuple(lst)
print(sum(lst))

# Task #2
text =("т","т","а","и","и","а","и")
tup=tuple(text)
print(text.count("т"))
print(text.count("а"))
print(text.count("и"))

#
#  Task #3

week_temp = ( 26, 29,34,32,28,28, 23)
sum_temp=sum(week_temp)
days=len(week_temp)
mean_temp=sum_temp/days
print(int(mean_temp))

# Домашняя работа

# Task #4

lst=[int(j) for j in input().split()]
tup=tuple(lst)
n=None
x=None
for i in range (len(tup)):
    if tup[i]==max(tup) and n==None:
        n=i
        print(n,'максимально:')
    elif tup[i]==min(tup) and x==None:
        x=i
        print(x,'минимально:')
print(tup,'количество элементов :', abs(n-x+1) if n<x else abs(n-x-1))


# Task # 5
tup=(-1,22,16,-18,1,9,5,-8,-5,-17,40,24,90,3)
lst=list(tup)
n=0
for i in range(len(tup)-1):
    if tup[i]>0 and tup[i+1]<0 or tup[i]<0 and tup[i+1]>0:
        n+=1
print(n)


#Task #3
tuple = (1, 2, 3, 4, 5, 6,8,45,34,90,4,52,6)
print( max(tuple) - min(tuple))


 # Task # 6
tup=(1,2,3,40,53,6,7,8,9,13,24,36,67,52,88,49,77,85,25,36,14,17,27,97)
count=0
for i in range (len(tup)):
    for k in range (2,i):
        if tup[i]%k==0:
            count+=1
            break
    if count==0 and tup[i]!=1:
        print(tup[i],end=' ')
    count=0



# Task #1
s=0
lst=[int(j) for j in input().split()]
tup=tuple(lst)
for k in tup:
    if k!= 1 and k!=0:
        for i in range (1,k):
            if k%i==0:
                s=s+i
        if s==k:
            print(k)
        s=0


# Task # 7
lst=[int(j) for j in input().split()]
tup=tuple(lst)
count=0
k=None
s=None
for i in range (len(tup)):
    if tup[i]==min(tup) and k==None :
        k=i
        print(k,'k')
    elif tup[i]==max(tup) and s==None:
     s=i
    print(s,'s')
count=abs(k-s)
print('количество элементов :', count-1)

# Домашнее заданее с 9 урока
# Task 10
lst=[int(i) for i in input().split( )]
for i in range (0,len(lst)):
  if i==lst.index(lst[i]) and lst.count(lst[i])>1:
      print(lst[i],end=' ')

# Task 11
lst=[]
count=0
for i in range(2,98):
     for j in range(2, i):
        if i%j==0:
         count+=1
        break
if count==0:
        lst.append(i)
        count =0
print(lst)
print([i for i in range(2,98) if i==2 or i==5 or i==3 or i==7 or i>9 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0])

# Task 12
lst=[int(j) for j in input().split( )]
s=''
for i in range (len(lst)-1,0,-1):
    lst.insert(i,0)
for l in lst:
  print(l,end=' ')

# Task 13
n=int(input('введите количество выводимых чисел'))
lst=[]
for i in range(1,100):
    for k in range (1,i+1):
        if len(lst) == n:
            break
            print(i,end=' ')
        lst.append(i)