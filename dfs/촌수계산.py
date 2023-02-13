import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

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

n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

answer = dijkstra(n1, n2)
if answer == INF:
    print(-1)
else:
    print(answer)