import sys
import heapq
input = sys.stdin.readline

n,k = map(int, input().split())
mv = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
mv.sort()
bag.sort()

ans = 0
tmp = []

for c in bag:
    while mv and mv[0][0] <= c:
        heapq.heappush(tmp, -heapq.heappop(mv)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
print(ans)