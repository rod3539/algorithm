import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(map(int, input().split()))
l, p = map(int, input().split())
