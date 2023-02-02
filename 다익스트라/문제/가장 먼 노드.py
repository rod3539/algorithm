from collections import deque

def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for a, b in edge:
        arr[a].append(b)
        arr[b].append(a)
    visited[1] = 1
    queue = deque([1])

    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

    answer = visited.count(max(visited))

    return answer if answer > 0 else 1