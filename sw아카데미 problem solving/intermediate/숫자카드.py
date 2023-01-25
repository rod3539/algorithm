T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(input())
    arr = [0] * 10
    count = -1
    answer = 0

    for i in range(10):
        for num in nums:
            if str(i) == num:
                arr[i] += 1

    for i in range(10):
        if count <= arr[i]:
            count = arr[i]
            answer = i

    print(f'#{tc} {answer} {count}')
