from heapq import heappop, heappush
import sys
input = sys.stdin.readline
cards = []
result = 0

n = int(input())
for i in range(n):
    heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heappop(cards) + heappop(cards)
        result += plus
        heappush(cards, plus)
    print(result)