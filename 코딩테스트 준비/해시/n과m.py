def back_tracking():
    if len(stack) == m:
        print(' '.join(list(map(str, stack))))
    else:
        for num in range(1, n + 1):
            if num not in stack:
                stack.append(num)
                back_tracking()
                stack.pop()


n, m = map(int, input().split())
stack = []
back_tracking()