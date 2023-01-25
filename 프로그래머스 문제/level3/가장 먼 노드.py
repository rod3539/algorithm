from collections import deque

def solution(n, edge):
    answer = 0
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

    max_v = max(visited)
    answer = visited.count(max_v)

    return answer if answer > 0 else 1