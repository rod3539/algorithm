T = int(input())
for tc in range(1, T + 1):
    sen = input()
    for i in range(1, 11):
        if sen[0:i] == sen[i: 2 * i + 1]:
            print(f'#{tc} {30 // (i + 1)}')
            break
