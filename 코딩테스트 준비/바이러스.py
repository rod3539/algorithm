from collections import deque

N = int(input())
check = [0] * (N + 1)
Computer = [[] for _ in range(N + 1)]

for i in range(int(input())):
    a, b = map(int, input().split())
    Computer[a].append(b)
    Computer[b].append(a)

check[1] = 1
q = deque([1])
while q:
    x = q.popleft()
    for i in range(len(Computer[x])):
        if check[Computer[x][i]] == 0:
            q.append(Computer[x][i])
            check[Computer[x][i]] = 1

print(sum(check) - 1)