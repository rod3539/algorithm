#경로를 벗어나면 안되므로 경로 체크 함수를 만들어 줬다.
def dfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(start_x, start_y)]
    while stack:
        now_x, now_y = stack.pop()
        visited[now_y][now_x] = 1

        if maze[now_y][now_x] == 3:
            return 1

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and maze[ny][nx] != 1:
                visited[ny][nx] = 1
                stack.append((nx, ny))
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # 미로의 좌표
    visited = [[0] * N for _ in range(N)]
    start_x = 0
    start_y = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x = j
                start_y = i
                break
    result = dfs(start_x, start_y)
    print(f'#{tc} {result}')