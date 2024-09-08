def solution(N, K, flowers, operations):
    # answer에 꽃이 폈는지 없는지 계속 갱신하는 배열을 만들었다.
    answer = [[0] * N for _ in range(N)]
    # 처음 flowers에 꽃이 펴있는 위치를 answer에 갱신
    for i in range(N):
        for j in range(N):
            if flowers[i][j]:
                answer[i][j] = 1
    # operations 배열 중 [1]과 [2]가 나왔을 때, 연산을 수행하므로
    # operations 배열을 돌면서 [1]과 [2]가 나왔을 때 각각의 연산을 실시
    for i in range(len(operations)):
        # operations 배열에서 [1]이 나왔을 때
        if operations[i] == [1]:
            # flowers 배열에 물주는 과정을 진행
            for j in range(N):
                for k in range(N):
                    # flowers 배열에서 꽃이 없는 위치에는 물이 계속 들어갈 수 있음
                    if not flowers[j][k]:
                        flowers[j][k] = operations[i+j+1][k]
                    elif flowers[j][k] and not answer[j][k]:
                        flowers[j][k] += operations[i+j+1][k]
                    # flowers 배열에서 꽃이 있는 위치인 경우
                    else:
                        # 물주기를 했을 때, flowers가 가질 수 있는 물의 허용치를 넘으면 꽃이 죽는다.
                        if flowers[j][k] - operations[i+j+1][k] <= 0:
                            flowers[j][k] = 0
                            answer[j][k] = 0
                        # 아닌 경우에는 그만큼 물을 가지고 있으므로 물을 가질 수 있는 허용치를 빼준다.
                        else:
                            flowers[j][k] -= operations[i+j+1][k]
        # 꽃을 피우는 과정
        elif operations[i] == [2]:
            # flowers배열을 순회
            for j in range(N):
                for k in range(N):
                    # 만약 꽃이 없는 장소이며, 물을 10 이상 가지고 있으면 꽃이 핀다.
                    if not answer[j][k] and flowers[j][k] >= 10:
                        flowers[j][k] = flowers[j][k] // 2
                        answer[j][k] = 1
    return answer


print(solution(5, 3, [[0, 2, 0, 3, 5], [0, 0, 0, 0, 0], [7, 3, 5, 3, 3], [9, 9, 0, 0, 0], [0, 0, 0, 0, 0]], [[1], [11, 3, 5, 1, 4], [1, 12, 7, 5, 6], [9, 10, 21, 2, 0], [1, 7, 5, 8, 35], [6, 7, 9, 10, 15], [2], [1], [7, 1, 2, 6, 4], [3, 4, 10, 7, 3], [4, 5, 7, 7, 7], [1, 8, 5, 9, 3], [8, 3, 12, 7, 5]]))
print(solution(3, 1, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1], [2, 0, 2], [0, 0, 0], [2, 0, 2]]))