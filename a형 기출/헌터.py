from collections import deque
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * 30 for _ in range(30)]
    if N == 2:
        for i in range(2):
            sx, sy, d = arr[i][0] + 15, arr[i][1] + 15, arr[i][2]
            if d > 1:
                for i in range(4):
                    nx = sx + dx[i] * d
                    ny = sy + dy[i] * d
                    if 0 <= nx < 30 and 0 <= ny < 30:
                        visited[nx][ny] += 1
                for j in range(1, d):
                    for i in range(8):
                        nx = sx + dx[i] * j
                        ny = sy + dy[i] * j
                        if 0 <= nx < 30 and 0 <= ny < 30:
                            visited[nx][ny] += 1
            elif d == 1:
                for i in range(4):
                    nx = sx + dx[i]
                    ny = sy + dy[i]
                    if 0 <= nx < 30 and 0 <= ny < 30:
                        visited[nx][ny] += 1
    for i in range(30):
        for j in range(30):
            if visited[i][j] == 2:

    print(visited)