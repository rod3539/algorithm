import sys

def dfs(i, j):
    if j == c-1:
        return True
    for d in dx:
        if 0 <= i+d < r and not visited[i+d][j + 1] and arr[i+d][j + 1] == '.':
            visited[i+d][j + 1] = 1
            if dfs(i+d, j + 1):
                return True
    return False


r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [-1, 0, 1]
answer = 0
for i in range(r):
    if arr[i][0] == '.':
        if dfs(i, 0):
            answer += 1
print(answer)
