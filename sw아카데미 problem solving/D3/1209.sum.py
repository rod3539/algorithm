for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    diagonal = 0
    inv_diagonal = 0
    for i in range(100):
        result.append(sum(arr[i]))
        temp = 0
        for j in range(100):
            temp += arr[j][i]
            if i == j:
                diagonal += arr[i][j]
            if i + j == 99:
                inv_diagonal += arr[i][j]
        result.append(temp)
    result.append(diagonal)
    result.append(inv_diagonal)
    print(f'#{T} {max(result)}')

