# 다익스트라
from math import inf
from heapq import heappush, heappop


def dijkstra(n, graph, start):
    dist = [inf for _ in range(n)]  # start 기준의 거리행렬
    dist[start] = 0                 # 자기 자신으로 가는 간선은 0

    q = []
    heappush(q, [dist[start], start])           # 거리와 노드를 함께 큐에 삽입
    while q:                                    # (비용이 작은 노드를 먼저 선택)
        cur_dist, cur_dest = heappop(q)
        if dist[cur_dest] >= cur_dist:          # start에서 cur_dest로 가는 거리가
            for i in range(n):                  # 이미 저장된 거리보다 작을 때만 진행
                new_dist = cur_dist + graph[cur_dest][i]
                if new_dist < dist[i]:          # cur_dest를 거쳐 i로 가는 거리가
                    dist[i] = new_dist          # 이미 저장된 거리보다 작으면 갱신
                    heappush(q, [new_dist, i])  # 다음 인접한 노드를 고려하기 위해 큐에 삽입
    return dist


def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1   # 0부터 시작하는 인덱스
    graph = [[inf] * n for _ in range(n)]
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    # 다익스트라
    # 모든 노드에 대해 다익스트라를 수행하고,
    # 반환된 1차원 거리행렬을 append 해줌
    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))

    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, min_graph[s][k] + min_graph[k][a] + min_graph[k][b])

    return ans