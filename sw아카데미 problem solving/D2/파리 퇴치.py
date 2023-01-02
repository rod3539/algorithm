T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            answer = 0
            for ii in range(M):
                for jj in range(M):
                    answer += arr[i+ii][j+jj]
            if result < answer:
                result = answer
    print(f'#{tc} {result}')
