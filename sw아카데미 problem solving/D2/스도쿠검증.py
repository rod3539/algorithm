T = int(input())
for tc in range(1, T + 1):
    sudo = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row[sudo[i][j]] += 1
            col[sudo[j][i]] += 1

        for k in range(1, 10):
            if row[k] != 1:
                answer = 0
                break
            if col[k] != 1:
                answer = 0
                break

    for i in range(3):
        for j in range(3):
            box = [0] * 10
            for k in range(3):
                for l in range(3):
                    box[sudo[3*i+k][3*j+l]] += 1
            for k in range(1, 10):
                if box[k] != 1:
                    answer = 0
                    break
    print(answer)