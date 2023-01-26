T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = [0]*10
    arr.sort()
    max_arr = arr[-5:]
    min_arr = arr[:5]
    min_arr.sort(reverse=True)
    for i in range(10):
        if not i % 2:
            answer[i] = max_arr.pop()
        else:
            answer[i] = min_arr.pop()
    print(f'#{tc} {" ".join(map(str, answer))}')

