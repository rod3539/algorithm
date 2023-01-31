import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for i in arr[start]:
        if not visited[i]:
            dfs(i)



n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        if not arr[i]:
            count += 1
            visited[i] = 1
        else:
            dfs(i)
            count += 1
print(count)

