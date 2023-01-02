T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if last > arr[i]:
            count += last - arr[i]
        else:
            last = arr[i]
    print(f'#{tc} {count}')