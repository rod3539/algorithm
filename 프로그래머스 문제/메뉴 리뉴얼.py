from collections import deque
def bfs(place):
    start = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i, j))
    for s in start:
        queue = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                    if place[ny][nx] == 'O':
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer