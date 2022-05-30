#
# Task 1
school = {"9а": 23, "9б": 28, "9в": 27, "9м": 22, "9ф": 26, "9у": 31, "9л": 32}
school["9в"] = 35
school["9я"] = 41
del school["9м"]
print({sum(school.values())})
print(school)

#
# Task 2
synonyms={"чистый":"опрятный",
          "грязный":"запачканный",
          "магия":"волшебство"}
search=input("Введите слово:")
if search in synonyms:
     print(synonyms .get(search))
else:
    print("Нет такого синонима:")


#
#Task 3
book = dict()
nomer = input()
while nomer != '.':
    nomer = nomer.split()
    if len(nomer) == 2:
        name, number = nomer
        book[name] = number
    else:
        name = ''.join(nomer)
        print(book[name])
    data = input()

# Task 5
str = input().lower().split()
d = dict()
for i in str:
    if i not in d:
        d[i] = d.get(i, 0)
    d[i] += 1
for key in d.keys():
    print(key, d[key])

