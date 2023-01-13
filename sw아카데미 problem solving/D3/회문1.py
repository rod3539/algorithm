for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            a = ''
            b = ''
            for k in range(n):
                a += arr[i][j+k]
                b += arr[j+k][i]
            if a == a[::-1]:
                count += 1
            if b == b[::-1]:
                count += 1
    print(f'#{tc} {count}')


