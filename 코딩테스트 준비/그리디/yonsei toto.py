import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
mile_sum = 0
subject = []
for _ in range(n):
    a, b = map(int, input().split())
    mile = list(map(int, input().split()))

    if b > a:
        heapq.heappush(subject, 1)
    else:
        mile.sort()
        i = a - b
        heapq.heappush(subject, mile[i])

for _ in range(len(subject)):
    mile_sum += heapq.heappop(subject)

    if m >= mile_sum:
        answer += 1
    else:
        break
print(answer)


