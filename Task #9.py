
 # Task # 1
n=int(input("enter num :"))
print([i for i in range(1,n+1) if i%2!=0])


 # Task #2
n=int(input())
print([i**2 for i in range(1,11)])


 # Task #3
n = int(input("enter num :"))
a = (sum([i for i in range(1000) if i%3 == 0 or  i%5 == 0]))
print(a)


 # Task #4
a = [int(i) for i in input().split()]
n = 1
for i in range(0, len(a) - 1):
     if a[i] != a[i + 1]:
         n += 1
print(n)

#
# Task # 5
a, b, c = map(int, input().split())
print([i ** c for i in range(a, b + 1)])



# # Task # 6
a = [int(i) for i in input().split()]
b = []
i = 0
if len(a) <= 1:
		b = a
else:
	while i < len(a) - 1:
		s = a[i - 1] + a[i + 1]
		b.append(s)
		i += 1
	b.append(a[0] + a[-2])
for k in b:
	print (k, end= " ")



# Task # 7
lst= [int (i) for i in input().split()]
lst.sort(reverse=True)
print(lst)


 # Task # 8
lst=[i for i in input ().split()]
lst.sort(key=len)
print(lst)


# Task # 9    # 2 варианта смотрите какой правильный
#1
lst=["aads"," adsd"," asdaa","adsds"]
lst.sort(key=lambda x:x.count("a",reverse= True))
lst2=sorted()
print(lst)
print(lst2)