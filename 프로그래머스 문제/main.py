import sys
import heapq
input = sys.stdin.readline

def solution(n, s, a, b, fares):
    answer = 1e9
    def djikstra(start):
        distance = [1e9] * (n + 1)
        queue = []
        heapq.heappush((0, start))
        distance[start] = 0
        while queue:
            dist, now = heapq.heappop(queue)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[0]
                if cost < distance[i[1]]:
                    heapq.heappush((cost, i[1]))
                    distance[i[1]] = cost
        return distance
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    # arr = [[]]
    # for k in range(1, n + 1):
    #     arr.append(djikstra(k))
    djikstra(s)

    return answer