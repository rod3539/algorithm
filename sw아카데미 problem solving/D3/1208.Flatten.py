for tc in range(1, 11):
    count = int(input())
    boxs = list(map(int, input().split()))

    while count:
        a = boxs.index((max(boxs)))
        boxs[a] -= 1
        b = boxs.index(min(boxs))
        boxs[b] += 1
        count -= 1

    print(f'#{tc} {max(boxs) - min(boxs)}')
