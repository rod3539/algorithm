import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
arr = [list(map(int, input().split())) for _ in range(w)]
p1 = [0, 0]
p2 = [n-1, n-1]
answer = 0
