T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_n = float('-inf')
    min_n = float('inf')
    for i in range(n-m+1):
        count = 0
        for j in range(m):
            count += arr[i + j]
        if count > max_n:
            max_n = count
        if count < min_n:
            min_n = count

    print(f'#{tc} {max_n - min_n}')

