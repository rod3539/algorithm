for tc in range(1, 11):
    n = int(input())
    bld = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(bld)-2):
        a = float('inf')
        arr = []
        for j in range(1, 3):
            if bld[i] <= bld[i+j]:
                a = 0
                arr.append(a)
                break
            elif bld[i] <= bld[i-j]:
                a = 0
                arr.append(a)
                break
            else:
                arr.append(bld[i]-bld[i+j])
                arr.append(bld[i]-bld[i-j])
        a = min(arr)
        answer += a
    print(f'#{tc} {answer}')

