import heapq
import sys

def dijkstra(start):
    queue = []
    distance = [int(1e9)] * (n + 1)
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
n, e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dis = dijkstra(s)

for i in range(1, n + 1):
    if dis[i] == int(1e9):
        print("INF")
    else:
        print(dis[i])