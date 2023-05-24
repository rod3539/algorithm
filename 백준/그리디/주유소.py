import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000001
answer = 0

for i in range(n-1):
    if price[i] < min_price:
        answer += road[i] * price[i]
        min_price = price[i]
    else:
        answer += road[i] * min_price

print(answer)