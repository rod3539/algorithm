N = int(input())
s, g, p, d = map(int, input().split())
mvp = input()
sum = 0
prev = 0

for i in range(N):
    if mvp[i] == 'B':
        sum += s - 1 - prev
        prev = s - 1 - prev
    elif mvp[i] == 'S':
        sum += g - 1 - prev
        prev = g - 1 - prev
    elif mvp[i] == 'G':
        sum += p - 1 - prev
        prev = s - 1 - prev
    