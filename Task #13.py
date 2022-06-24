# #
# import random # найти мин и макс и перевернуть
# A = [[random.randint(-100,100) for i in range(3) for  j in range(5)]]
# min_el= max_el= A[0][0]
# imin=jmin=imax=jmax= 0
# for i in range (len(A)):
#     for j in range (len(A[i])):
#         if min_el> A[i][j]:
#             min_el=A[i][j]
#             imin=i
#             jmin=j
#         if max_el< A[i] [j]:
#             max_el= A[i][j]
#             imax=i
#             jmax=j
#             print()
#             print(max_el,min_el)
# A[imin][jmin],A[imax,imin]=A[imax,imax]

#
# Task 2
n = int(input())
k = [['.'] * n for i in range(n)]
for i in range(n):
    k[i][i] = '*'
    k[n // 2][i] = '*'
    k[i][n // 2] = '*'
    k[i][n - i - 1] = '*'
for row in k:
    print(' '.join(row))


#
# Task #3
n, m = [int(i) for i in input().split()]
s = []
for i in range(n):
    s.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            s[i].append('.')
        else:
            s[i].append('*')
for row in s:
    print(' '.join(row))


#
# Task #7
x = (1, 2, 5, 7)
try:
    x = x  / 2
    print(x)
except TypeError:
    print('TypeError')

#
# Task #14
dict ={"key1":"value1","key2":"value2","key3":"value3"}
key = "Нет ключа"
try:
    print(dict[key])
except KeyError:
    print("ValueError")

#
# Task #8
my_list = ["Python","C","C++","JavaScript"]
search_idx = 6
try:
    print(my_list[search_idx])
except IndexError:
    print("IndexError")

#
# Task # 13
try:
    num = int(input("Введите число: "))
    print("Все верно. Число:", num)
except ValueError:
    print("Это не число.")

# Task #6 (где-то ошибка все время No)
a = int(input())
m = []
for i in range(a):
   m.append([int(g) for g in input().split()])
for i in range(a):
   is_break = False
   for g in range(i):
       if m[i][g] != m[g][i]:
           print('NO')
           is_break = True
           break
   if is_break:
       break
else:
     print('YES')