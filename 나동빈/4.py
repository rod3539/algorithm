def solution(N, K, flowers, operations):
    answer = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if flowers[i][j]:
                answer[i][j] = 1
    for i in range(len(operations)):
        if operations[i] == [1]:
            for j in range(N):
                for k in range(N):
                    if not flowers[j][k]:
                        flowers[j][k] = operations[i+j+1][k]
                    elif flowers[j][k] and not answer[j][k]:
                        flowers[j][k] += operations[i+j+1][k]
                    else:
                        if flowers[j][k] - operations[i+j+1][k] <= 0:
                            flowers[j][k] = 0
                            answer[j][k] = 0
                        else:
                            flowers[j][k] -= operations[i+j+1][k]
        elif operations[i] == [2]:
            for j in range(N):
                for k in range(N):
                    if not answer[j][k] and flowers[j][k] >= 10:
                        flowers[j][k] = flowers[j][k] // 2
                        answer[j][k] = 1
    return answer