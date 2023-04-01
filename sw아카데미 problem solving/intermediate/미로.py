from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, count):
    queue = deque()
    queue.append((x, y, count))
    visited[x][y] = 1
    while queue:
        nx, ny, idx = queue.popleft()
        if maze[nx][ny] == '2':
            return idx - 1
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]
            if 0 <= xx < n and 0 <= yy < n and maze[xx][yy] != '1' and not visited[xx][yy]:
                queue.append((xx, yy, idx + 1))
                visited[xx][yy] = 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '3':
                answer = bfs(i, j, 0)

    print(f'#{tc} {answer}')