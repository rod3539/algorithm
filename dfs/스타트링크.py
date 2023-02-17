import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        x = queue.popleft()
        if x == g:
            return count[g]
        for i in (x+u, x-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[x] + 1
                queue.append(i)
    if not count[g]:
        return "use the stairs"


f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
count = [0] * (f + 1)
print(bfs(s))