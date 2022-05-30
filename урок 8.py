a = [4,6,'pу','tell',78]
b = [44,"hello",56,"exept",3]
c=a+b
c.insert (3,6)
i=0
while i< len(c) :
    print(c[i])
    if isinstance(c[i],str) :
        del c [i]
    else:
            i+=1
print(*c)    # без квадратных скобок