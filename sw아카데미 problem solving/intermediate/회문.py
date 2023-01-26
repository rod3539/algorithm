T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    answer = ''
    for i in range(n):
        for j in range(n-m+1):
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                answer = arr[i][j:j + m]
                print(f'#{tc} {answer}')
                break

    if not answer:
        for j in range(n):
            for k in range(n-m+1):
                a = ''
                for i in range(m):
                    a += arr[i+k][j]
                if a == a[::-1]:
                    print(f'#{tc} {a}')