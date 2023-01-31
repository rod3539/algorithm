import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    count = 1
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                count += 1
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return count




n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
starts = []
for i in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    starts.append((a-1, b-1))
a = 0
for start in starts:
    visited[start[0]][start[1]] = 1
    b = bfs(start)
    if a < b:
        a = b

print(a)
