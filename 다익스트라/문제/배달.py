from heapq import heappush, heappop
def solution(N, road, K):
    INF = int(1e9)
    def dijkstra(start, end):
        distance = [INF] * (N + 1)
        queue = []
        heappush(queue, (0, start))
        distance[start] = 0
        while queue:
            dist, now = heappop(queue)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heappush(queue, (cost, i[0]))
        return distance[end]
    answer = 1
    graph = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    for i in range(2, N+1):
        count = dijkstra(1, i)
        print(count)
        if count <= K:
            answer += 1
    return answer