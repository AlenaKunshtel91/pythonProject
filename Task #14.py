# #
# f=open("test1.txt","w",encoding="utf-8")
# s=input("enter string:")
# f.write("help me  \n ")
# f.write( s+"\n")
# f.write("Nello world")
import wsgiref.validate

# #
# d={
#     "Иванов Иван ": [ 2,3,4,6,],
#     "Сидоров Петя ":[2,9,8,6,4],
#     "Петров Иван ":[4,3.9,5]
# }
# for key, value in d.items():
#          f.write(key + " :")
# f.el in value:
#     f.write(str(el + " "))
#     f.write( "\n")

#
# Task # 1
my_file = open("baby_file.txt", "w", encoding="utf-8")
for i in range(6):
    a = input("Ввести текст:")
    my_file.writelines(a + "\n")
my_file.close()

#
# Task # 2
text = input("\n")
output = " "
with open("baby_file.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        output += (text + "\n")
with open("baby_file.txt", "a", encoding="utf-8") as my_file:
    my_file.write(output)

# Task #2
text=input()
for i in range (3):
     with open("baby_file.txt","a",encoding= "utf-8") as my_file :
      my_file.write (text +"\n")
my_file.close()

#
#Task#3
f=" "
with open("baby_file.txt","r",encoding= "utf-8") as my_file:
    for line in my_file:
        f1=my_file.read().rstrip()
        f+=f1
        print(len(f))


# Task # 4
lst=[]
n= " "
with open("baby_file.txt", "r", encoding="utf-8") as my_file:
    n=my_file.readline().rstrip()
    lst.append(n)
    n = my_file.readline().rstrip()
    lst.append(n)
    n=my_file.readline().rstrip()
    lst.append(n)
    n=my_file.readline().rstrip()
    lst.append(n)
    n=my_file.readline().rstrip()
    lst.append(n)
    print(lst)

#
# Task #5
with open("baby_file.txt", "r", encoding="utf-8") as my_file:
    n=my_file.read()
print(n.replace("\n","!\n") if n[-1]=="\n" else(n.replace(("\n","!\n")+"!")))
print()


#
# Task#6
l=0
number=0
max=0
n=" "
with open("baby_file.txt", "r", encoding="utf-8") as my_file:
    for i in my_file:
        s=i.strip()
        number+=1
        if len(s)>1:
            l=len(s)
        max=number
        n=s
print ( f" самая длинная строка : {max} : {n} : ее длина {l} символов " )

