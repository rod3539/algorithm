from collections import deque

def bfs(start, end, idx):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((start, end))
    visited[start][end] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] > idx:
                queue.append((nx, ny))
                visited[nx][ny] = 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = []
for k in range(max(map(max, arr))):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                count += 1
    answer.append(count)
print(max(answer))