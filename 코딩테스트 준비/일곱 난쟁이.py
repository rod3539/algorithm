from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))
com = list(combinations(arr, 7))
for i in range(len(com)):
    if sum(com[i]) == 100:
        result = sorted(com[i])
for i in range(7):
    print(result[i])