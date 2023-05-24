def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = []
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        visited = [0] * (n + 1)
        queue = []
        queue.append(start)
        count = 0
        visited[start] = 1
        while queue:
            x = queue.pop()
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    count += 1
        return count

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer.append(abs(bfs(a) - bfs(b)))
        graph[a].append(b)
        graph[b].append(a)


    return min(answer)