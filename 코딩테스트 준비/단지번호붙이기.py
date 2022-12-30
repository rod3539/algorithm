from collections import deque
from collections import Counter
from functools import reduce

# 입력받기
n = int(input())

# 지도 입력받기 (2차원)
a = [list(map(int, list(input()))) for _ in range(n)]

# 방문 체크용 리스트 (2차원)
group = [[0] * n for _ in range(n)]

# 위 아래 왼 오 방향이동용 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()

        # 위 아래 왼쪽 오른쪽 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 지도 밖으로 안 나갔는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 집이 있고, 아직 방문한 곳이 아니라면 꼬우
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


# 모든 정점을 시작점으로 해서 탐색
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

# 단지수 출력
print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기
ans = reduce(lambda x, y: x + y, group)
# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str, ans)))