
def bfs():
    queue = []
    count = 0
    queue.append(1)
    visited[1] = 1
    while queue:
        x = queue.pop()
        for i in arr[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                count += 1
    return count


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
answer = bfs()
print(answer)
