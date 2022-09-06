from collections import deque

def dfs(V):
    visited_dfs[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    q = deque()
    q.append(V)
    visited_bfs[V] = 1
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited_bfs[i] and graph[V][i]:
                q.append(i)
                visited_bfs[i] = 1

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited_bfs = [0] * (N + 1)
visited_dfs = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

bfs(V)