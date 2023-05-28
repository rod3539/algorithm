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


print(solution(5, 3, [[0, 2, 0, 3, 5], [0, 0, 0, 0, 0], [7, 3, 5, 3, 3], [9, 9, 0, 0, 0], [0, 0, 0, 0, 0]], [[1], [11, 3, 5, 1, 4], [1, 12, 7, 5, 6], [9, 10, 21, 2, 0], [1, 7, 5, 8, 35], [6, 7, 9, 10, 15], [2], [1], [7, 1, 2, 6, 4], [3, 4, 10, 7, 3], [4, 5, 7, 7, 7], [1, 8, 5, 9, 3], [8, 3, 12, 7, 5]]))
print(solution(3, 1, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1], [2, 0, 2], [0, 0, 0], [2, 0, 2]]))