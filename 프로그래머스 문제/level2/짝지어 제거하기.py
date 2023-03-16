def solution(s):
    stack = []

    for w in s:
        if not stack:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    if not stack:
        return 1
    else:
        return 0

print(solution('baabaa'))
print(solution('cdcd'))
