import sys
from collections import deque
input = sys.stdin.readline
def bfs(a, b, color):
    count = 0
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count + 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]
w = 0
b = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W' and not visited[i][j]:
            w += bfs(i, j, 'W') ** 2
        elif arr[i][j] == 'B' and not visited[i][j]:
            b += bfs(i, j, 'B') ** 2
print(w, b)
