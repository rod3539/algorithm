def solution(n, wires):
    answer = []
    arr = [[] for _ in range(n+1)]
    for a, b in wires:
        arr[a].append(b)
        arr[b].append(a)

    def bfs(start):
        visited = [0] * (n + 1)
        queue = []
        queue.append(start)
        count = 0
        visited[start] = 1
        while queue:
            x = queue.pop()
            for i in arr[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    count += 1
        return count

    for a, b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        answer.append(abs(bfs(a) - bfs(b)))
        arr[a].append(b)
        arr[b].append(a)


    return min(answer)
