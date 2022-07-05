N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))

stack = []
result = []
for i in range(N-1, -1, -1):
    building = buildings[i]
    if stack:
        if stack[-1][0] > building:
            result.append(stack[-1][1])
            stack.append((building, i+1))
        else:
            while stack and stack[-1][0] <= building:
                stack.pop()
            if stack:
                result.append(stack[-1][1])
            else:
                result.append(0)
            stack.append((building, i+1))
    else:
        result.append(0)
        stack.append((building, i+1))

answer = list(reversed(result))
for ans in answer:
    print(ans)