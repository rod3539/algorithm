T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    decode = {'0001101': 0, '0011001':1, '0010011':2, '0111101':3,
              '0100011':4, '0110001':5, '0101111':6, '0111011':7,
              '0110111':8, '0001011':9}
    code = []
    all_code = []
    answer = 0
    result = 0
    for i in range(n):
        if '1' in arr[i]:
            for j in range(m-1, -1, -1):
                if arr[i][j] == '1':
                    for k in range(56):
                        code.append(arr[i][j-k])
            break
    for i in range(55, -1, -7):
        a = ''
        for j in range(7):
            a += code[i - j]
        all_code.append(a)

    for i in range(8):
        if not i % 2:
            answer += decode.get(all_code[i]) * 3
            result += decode.get(all_code[i])
        else:
            answer += decode.get(all_code[i])
            result += decode.get(all_code[i])
    if not answer % 10:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {0}')


