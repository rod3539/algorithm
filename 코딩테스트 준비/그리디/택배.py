import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])

box = [c] * (n + 1)
answer = 0
for s, e, b in arr:
    _min = c
    for i in range(s, e):
        _min = min(_min, box[i])
    _min = min(_min, b)
    for i in range(s, e):
        box[i] -= _min
    answer += _min
print(answer)