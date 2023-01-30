import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[n-1][m-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(bfs())