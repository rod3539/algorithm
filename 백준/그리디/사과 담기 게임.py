import sys
input = sys.stdin.readline()

n = int(input)
arr = [int(input) for _ in range(n)]

arr.sort(reverse=True)
result = []

for i in range(n):
    result.append(arr[i] * (i + 1))

print(max(result))