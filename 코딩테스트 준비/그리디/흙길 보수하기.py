import sys
input = sys.stdin.readline
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
plank = arr[0][0]
answer = 0
for start, end in arr:
    if plank > end:
        continue
    elif plank < start:
        plank = start
    dist = end - plank
    remainder = 1
    if not dist % l:
        remainder = 0
    count = dist // l + remainder
    plank += count * l
    answer += count
print(answer)


