import heapq
import sys

def dijkstra(start):
    queue = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

dis_1 = dijkstra(1)
dis_v1 = dijkstra(v1)
dis_v2 = dijkstra(v2)
path1 = dis_1[v1] + dis_v1[v2] + dis_v2[n]
path2 = dis_1[v2] + dis_v2[v1] + dis_v1[n]

result = min(path2, path1)
print(result if result < INF else -1)