from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    count = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    count += 1
    return count + 1




N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

B, W = 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'W':
                W += bfs(i, j, 'W') ** 2
            else:
                B += bfs(i, j, 'B') ** 2
print(W, B)
