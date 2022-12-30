from collections import deque
def bfs(start):
    global result
    queue = deque()
    queue.append(start)
    arr[start] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            result += 1
            continue
        for nx in (x * 2, x + 1, x - 1):
            if 0 <= nx < 100001 and (arr[nx] == arr[x] + 1 or arr[nx] == -1):
                arr[nx] = arr[x] + 1
                queue.append(nx)


n, k = map(int, input().split())
arr = [-1] * 100001
result = 0
bfs(n)

print(arr[k])
print(result)
