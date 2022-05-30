
 # Task #1
s = input()
print(s[3])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

""
""
# Task #5
s = "Яблоко"
print(s[1:5])
print(s[3::1])
""
""
# Task# 3
s = input()
if s[0]==s[-1]:
    print('Yes!')
else: print('No!')
""
""
# Task # 10
s=input()
print(s.replace("1","one "))
""
""
# Task # 7

""
""
Task # 8
s="Hello fish"
print(s.index ("f"))
print(s.count("f"))
""
# Task # 12
s = "192.168.0.1"
print(s.replace(".", " "))
a=int(s[0:3])
b=int( s[4:7])
c= int(s[8])
d=int( s[10])
print(f" {a+b+c+d}")
""
""
# Task #8 еще один вариант
s= "Hello fish"
if "f" in s:
    print(s.count("f"))
""
""
# Task # 6
n="*"
print(n * 5 )
""
""
# Task # 11   # никак 40 не получается, 22 и все???????
s = "aCggGttat"
print((s.count('c')+s.count('g')+s.count('G')/len(s)*100 ))
""
""
# Task #9
s = input("Данно слово :")
print(s. find("f"))
if "f" in s:
    print( -1 )
if "f" not in s:
    print( -2 )
""
""
# Task # 4 #  наверное не правильно поняла условие ?????
s = input("Дано слово :")
s2 = "2 " + s[2:]
s3 = "3 " + s[3:]
s4 = "4 " + s[4:]
print(f"{s2} {s3} {s4}")
""