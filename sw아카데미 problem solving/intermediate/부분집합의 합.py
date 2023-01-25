from itertools import combinations
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    answer = 0
    for i in range(1, 13):
        arr.append(i)
    result = list(combinations(arr, n))

    for i in result:
        if sum(i) == k:
            answer += 1

    print(f'#{tc} {answer}')