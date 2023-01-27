T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    stack = []
    for i in range(len(arr)):
        if not stack:
            if arr[i] == '}' or arr[i] == ')':
                stack.append(arr[i])
                break
        if arr[i] == '{' or arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(arr[i])
        elif arr[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(arr[i])
    if not stack:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
