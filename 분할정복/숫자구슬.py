N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = max(arr)
e = sum(arr)
result = []
min_value = sum(arr)

while s <= e:
    mid = (s + e) // 2
    total = 0