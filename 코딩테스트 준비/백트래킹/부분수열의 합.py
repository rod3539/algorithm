from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(1, N + 1):
    coms = list(combinations(arr, i))
    for com in coms:
        if sum(com) == S:
            count += 1
print(count)
