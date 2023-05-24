from collections import deque
def solution(n, computers):
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = 1
        while queue:
            s = queue.popleft()
            for k in range(len(computers[s])):
                if computers[s][k] == 1 and not visited[k]:
                    visited[k] = 1
                    queue.append(k)


    visited = [0] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            print(visited)
    return answer

