N = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(N-1, 0, -1):
    if stack:
        stack[-1] > arr[i]

