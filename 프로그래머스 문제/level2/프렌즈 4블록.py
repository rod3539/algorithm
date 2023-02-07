def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        # 같은 모양의 2x2블록을 찾으면 rm배열에 1 표시
        rm = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    rm[i][j], rm[i][j+1], rm[i+1][j], rm[i+1][j+1] = 1, 1, 1, 1
        # 지워진 블록 개수 세기
        count = 0
        for i in range(m):
            count += sum(rm[i])
        answer += count
        if not count:
            break
        # 지워진 블록을 위 블록으로 채우기
        for i in range(m-1, -1, -1):
            for j in range(n):
                if rm[i][j] == 1:
                    x = i-1
                    while x >= 0 and rm[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        rm[x][j] = 1

    return answer