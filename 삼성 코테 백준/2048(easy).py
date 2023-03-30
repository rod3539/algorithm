import sys
from copy import deepcopy

input = sys.stdin.readline


def move(board, dir):
    if dir == 0:  # 위
        for j in range(N):
            pointer = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]  # 현재 보드의 값
                    board[i][j] = 0
                    if board[pointer][j] == 0:  # 포인터가 가리키는 수가 0일 때
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:  # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                        board[pointer][j] *= 2
                        pointer += 1
                    else:  # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                        pointer += 1
                        board[pointer][j] = tmp
    elif dir == 1:  # 아래
        for j in range(N):
            pointer = N - 1
            for i in range(N - 2, -1, -1):  # n-1, n-2, ..., 1, 0
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] = tmp * 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    elif dir == 2:  # 오른쪽
        for i in range(N):
            pointer = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] = tmp * 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
    else:  # 왼쪽
        for i in range(N):
            pointer = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] = tmp * 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    for i in range(4):  # 상,하,좌,우
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(graph, 0)
print(ans)