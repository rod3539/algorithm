def dfs(start, end):
    stack = []
    visited = [0] * (V+1)
    stack.append(start)
    while stack:
        now = stack.pop()
        visited[now] = 1
        for next in range(1, V+1):
            if not visited[next] and node[now][next]:
                stack.append(next)
    if visited[end]:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, G)}')