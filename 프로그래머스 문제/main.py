def solution(m, n, board):
    answer = 0
    # block = ['R', 'M', 'A', 'F', 'N', 'T', 'J', 'C']
    for i in range(m):
        board[i] = list(board[i])
    while True:
        rm = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == board[i][j+1] and  board[i][j] == board[i+1][j+1] and board[i][j] == board[i+1][j] and board[i][j]:
                    rm[i][j] = 1
                    rm[i+1][j] = 1
                    rm[i][j+1] = 1
                    rm[i+1][j+1] = 1
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






print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
