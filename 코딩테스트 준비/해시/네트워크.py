def solution(n, computers):
    answer = 0
    visited = [0] * n
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1
    return answer
def dfs(n, computers, com, visited):
    visited[com] = 1
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if not visited[connect]:
                dfs(n, computers, connect, visited)