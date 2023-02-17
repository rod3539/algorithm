from itertools import combinations
arr = []
for i in range(9):
    a = int(input())
    arr.append(a)
a = list(combinations(arr, 7))
b = []
for i in a:
    if sum(i) == 100:
        for k in i:
            b.append(k)
        break
b.sort()
for i in range(7):
    print(b[i])

