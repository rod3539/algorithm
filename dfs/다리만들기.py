import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline

def find_island(i, j, idx):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    arr[i][j] = idx
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                arr[nx][ny] = idx
                visited[nx][ny] = 1
                queue.append((nx, ny))

def find_dist(idx):
    global answer
    queue = deque()
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == idx:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] and arr[nx][ny] != idx:
                    answer = min(answer, dist[x][y])
                    return
                if not arr[nx][ny] and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
count = 1
answer = sys.maxsize
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            count += 1
            find_island(i, j, count)

for i in range(2, count+1):
    find_dist(i)
print(answer)
