from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    INF = int(1e9)
    def dijkstra(start):
        distance = [INF] * (n + 1)
        queue = []
        heappush(queue, (0, start))
        distance[start] = 0
        while queue:
            dist, now = heappop(queue)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(queue, (cost, i[0]))
        return distance



    answer = INF
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare[0], fare[1], fare[2]
        graph[c].append((d, f))
        graph[d].append((c, f))
    dist_graph = []
    for i in range(1, n+1):
        dist_graph.append(dijkstra(i))
    for k in range(1, n+1):
        answer = min(answer, dist_graph[s-1][k] + dist_graph[k-1][a] + dist_graph[k-1][b])
    return answer

