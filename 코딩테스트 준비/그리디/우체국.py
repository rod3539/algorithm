import sys
input = sys.stdin.readline
n = int(input())
arr = []
pop = 0
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    pop += b

arr.sort(key=lambda x:x[0])
mid = pop // 2
if pop % 2:
    mid += 1

count = 0
for a, b in arr:
    count = count + b
    if count >= mid:
        answer = a
        break
print(answer)