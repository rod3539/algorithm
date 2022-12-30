import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for i in range(N)]

# 맨 윗줄
for j in range(1, M):
    board[0][j] += board[0][j - 1]

# 나머지
for i in range(1, N):
    startLeft = [board[i][j] + board[i - 1][j] for j in range(M)]
    startRight = [board[i][j] + board[i - 1][j] for j in range(M)]

    # →
    for j in range(1, M):
        startLeft[j] = max(startLeft[j], startLeft[j - 1] + board[i][j])

        # ←
    for j in range(M - 2, -1, -1):
        startRight[j] = max(startRight[j], startRight[j + 1] + +board[i][j])

    # 선택
    for j in range(M):
        board[i][j] = max(startLeft[j], startRight[j])

print(board[-1][-1])