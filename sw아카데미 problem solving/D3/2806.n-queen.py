def nQueen(k):
    if k == N:
        global answer
        answer += 1
    else:
        for i in range(N):
            a, b = k + i, k - i + N - 1
            if col[i] or line1[a] or line2[b]:
                continue
            col[i] = line1[a] = line2[b] = 1
            nQueen(k + 1)
            col[i] = line1[a] = line2[b] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    col = [0] * N
    line1 = [0] * (N * 2 - 1)
    line2 = [0] * (N * 2 - 1)
    answer = 0
    nQueen(0)
    print('#{} {}'.format(tc, answer))