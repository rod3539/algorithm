for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    for i in range(n):
        y, x = 0, i
        stack = []
        while y < n:
            if not stack and arr[y][x] == 1:
                stack.append(1)
            elif stack and arr[y][x] == 2:
                count += stack.pop()
            y += 1
    print(f'#{tc} {count}')