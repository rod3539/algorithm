T = int(input())
for tc in range(1, T + 1):
    sen = input()
    if sen == sen[::-1]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')