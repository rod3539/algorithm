import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
        print(0)
        continue
    visited = [[0] * l for _ in range(l)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 1
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    answer = 0
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            answer = visited[x][y] - 1
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    print(answer)
