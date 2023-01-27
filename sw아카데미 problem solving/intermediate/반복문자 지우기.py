T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []
    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
        else:
            if stack[-1] == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
    print(f'#{tc} {len(stack)}')
