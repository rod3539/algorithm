import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in range(n):
    a = arr[i] - b
    answer += 1
    if a <= 0:
        continue
    if not a % c:
        answer += a // c
    else:
        answer += a // c + 1
print(answer)