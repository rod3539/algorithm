from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    answer = 1e9

    def djikstra(start):
        distance = [1e9] * (n + 1)
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

    graph = [[] for _ in range(n+1)]
    for c, d, e in fares:
        graph[c].append((d, e))
        graph[d].append((c, e))
    arr = [[]]
    for i in range(1, n + 1):
        arr.append(djikstra(i))
    for i in range(1, n+1):
        answer = min(answer, arr[s][i] + arr[i][a] + arr[i][b])

    return answer