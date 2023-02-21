def solution(m, n, puddles):
    puddles = [[b-1, a-1] for a, b in puddles]
    arr = [[0] * m for _ in range(n)]
    arr[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [i, j] in puddles:
                arr[i][j] = 0
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]

    return arr[i][j] % 1000000007