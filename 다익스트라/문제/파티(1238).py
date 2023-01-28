import sys
import heapq

def dijkstra(start, end):
    queue = []
    distance = [INF] * (n + 1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance[end]


input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = [0] * (n + 1)
for i in range(1, n + 1):
    result[i] += dijkstra(i, x)
    result[i] += dijkstra(x, i)
print(max(result))