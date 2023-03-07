from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]
        for nx in (x * 2, x-1, x+1):
            if 0 <= nx <= m and not dist[nx]:
                if nx == x * 2:
                    dist[nx] = dist[x]
                    queue.append(nx)
                else:
                    dist[nx] = dist[x] + 1
                    queue.append(nx)

n, k = map(int, input().split())
m = 10 ** 5
dist = [0] * (m + 1)
print(bfs(n, k))

