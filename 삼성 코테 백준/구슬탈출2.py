from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))
    visited = []
    count = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10:
                print(-1)
                return
            if maze[rx][ry] == 'O':
                print(count)
                return
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if maze[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if maze[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if maze[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if maze[nbx][nby] == 'O':
                        break
                if maze[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)


n, m = map(int, input().split())
maze = [list(map(str, input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'R':
            rx, ry = i, j
        elif maze[i][j] == 'B':
            bx, by = i, j
bfs(rx, ry, bx, by)
