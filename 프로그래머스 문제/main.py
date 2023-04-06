def solution(n, computers):
    answer = 0

    # 그래프 넣기
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i + 1].append(j + 1)

    return answer
