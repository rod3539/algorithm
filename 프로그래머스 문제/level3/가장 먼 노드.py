from heapq import heappop, heappush
def solution(n, edge):

    def djikstra():
        distance = [1e9] * (n + 1)
        queue = []
        heappush(queue, (0, 1))
        distance[1] = 0
        while queue:
            dist, now = heappop(queue)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if not visited[i[0]] and cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(queue, (cost, i[0]))

        return distance[1:n+2].count(max(distance[1:n+2]))



    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    answer = djikstra()

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))