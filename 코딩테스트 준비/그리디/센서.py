import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
dist = []

if k >= n:
    print(0)
else:
    for i in range(n-1):
        dist.append(arr[i+1] - arr[i])
    dist.sort()
    for _ in range(k-1):
        dist.pop()

    print(sum(dist))