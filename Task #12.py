#
# Task 1
set = {1, 8, 7, 6, 9, 0, 5, 7, 6, 5, 7, 6}
print(len(set))

# Task 2
set = {1, 2, 3, 4, 5, 6, 6, 7}
set2 = {2, 9, 8, 7, 6, 5, 4, 5}
output = set & set2
print(len(output))

# Task 3
set = {1, 2, 3, 4, 5, 6, 7, 9}
set2 = {9, 8, 7, 6, 5, 4, 3, 2, 1}
output = (set & set2)
print(len(output), set.symmetric_difference(set2))

#
#Task #4
L = [int(i) for i in input().split()]
S = set()
for i in L:
    if i in S:
        print('YES')
    else:
        print('NO')
    S.add(i)

#
# Task #6
n = int(input())
nums = set(range(1, n + 1))
possible_nums = nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible_nums & guess) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= guess
    else:
        print('NO')
        possible_nums &= nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))





