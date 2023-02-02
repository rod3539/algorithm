

def dfs(v):
    visited[v] = 1
    number = numbers[v]
    if not visited[number]:
        dfs(number)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [1] + [0] * N
    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)