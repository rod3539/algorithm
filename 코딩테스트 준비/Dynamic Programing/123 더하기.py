def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        arr = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    arr[i][j] = 1
                    arr[i+1][j] = 1
                    arr[i][j+1] = 1
                    arr[i+1][j+1] = 1

        count = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j]:
                    count += 1
        if not count:
            break
        answer += count

        for i in range(m-1, -1, -1):
            for j in range(n):
                if arr[i][j]:
                    x = i - 1
                    while x >= 0 and arr[x][j]:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        arr[x][j] = 1

    return answer