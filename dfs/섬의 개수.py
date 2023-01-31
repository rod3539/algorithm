import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y, w, h):

    queue = deque()
    queue.append((x,y))
    island[x][y] = 2

    while queue:
        cx, cy = queue.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                island[nx][ny] = 2
                queue.append((nx, ny))
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                cnt += bfs(i, j, w, h)
    print(cnt)