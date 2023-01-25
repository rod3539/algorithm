T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    answer = 0
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2+ 1):
            for k in range(c1, c2 + 1):
                arr[j][k] += color

    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                answer += 1


    print(f'#{tc} {answer}')

