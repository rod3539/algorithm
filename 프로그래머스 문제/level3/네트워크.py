def solution(n, computers):

    def bfs(start):
        queue = [start]
        visited[start] = 1
        while queue:
            now = queue.pop()
            for i in graph[now]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)


    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    answer = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer