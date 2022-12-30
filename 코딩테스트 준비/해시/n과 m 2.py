n, m = map(int, input().split())
stack = []
def back(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(start, n + 1):
        if i not in stack:
            stack.append(i)
            back(i + 1)
            stack.pop()
back(1)