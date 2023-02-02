from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, idx):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == '1':
                idx += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return idx

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            home.append(bfs(i, j, 1))
print(len(home))
home.sort()
for h in home:
    print(h)

