from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = visited[nx][ny] + 1


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs()
print(visited[-1][-1])