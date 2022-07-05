N = int(input())
stack = []
result = 0
for _ in range(N):
    cow = int(input())
    if stack:
        if stack[-1] > cow:
            result += len(stack)
            stack.append(cow)
        else:
            while stack and stack[-1] <= cow:
                stack.pop()
            result += len(stack)
            stack.append(cow)
    else:
        stack.append(cow)
print(result)
