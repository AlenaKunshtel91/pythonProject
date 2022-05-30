# ""
# a = False
# b = True
# if a :
#     print("Yes")
# ""
# ""
# s = input()
# print(s[4::-2])
# ""

s = "hjed@poe"
ind = s.find("@")
print(ind)
s2 = s[ind + 1:] + s[ind] + s[:ind]
print(s2)

s= "hello world"
print(s[:5])
