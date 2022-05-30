# # Task #3
with open('baby_file.txt') as f1:
    f1_lines = f1.read().splitlines()
with open('baby_file.txt', 'w') as f2:
    for line in f1_lines[::-1]:
        f2.write('%s\n' % line)

# Task 4
text = open("baby_file.txt").read()
unique = set(text.split())
for word in unique:
    print(f'{word}: {text.count(word)}')

# Task #5
r = [[1, 2, 4, 7, 9, 6], [1, 16, 3, 8, 1, 41 ]]
for row in r:
    res = max([int(i) for i in row if i in r[0] and i in r[1]])
print(res)
