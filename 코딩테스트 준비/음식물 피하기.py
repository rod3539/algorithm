from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i):
    global count
    count = 1
    queue = deque()
    queue.append(i)
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                count += 1
                visited[nx][ny] = 0
                queue.append((nx, ny))


n, m, k = map(int ,input().split())
visited = [[0]*m for _ in range(n)]
trash = []
result = float('-inf')
count = 1

for _ in range(k):
    x, y = map(int, input().split())
    visited[x-1][y-1] = 1
    trash.append((x-1, y-1))
for i in trash:
    bfs(i)
    if result < count:
        result = count
print(result)

