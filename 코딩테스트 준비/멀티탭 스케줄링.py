from collections import deque
def dfs(v):
    print(str(v), end=" ")
    if v == m:
        return
    else:
        for i in range(1, n + 1):
            if map[v][i] == 1 and check[i] == 0:
                check[i] = 1
                dfs(i)


n, m, v = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n + 1)]
check = [0] * (n + 1)
check_bfs = [0] * (n + 1)
for i in range(m):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1

check[v] = 1
dfs(v)



