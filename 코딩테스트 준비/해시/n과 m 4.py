n, m = map(int, input().split())
stack = []
def back(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(start, n + 1):
        stack.append(i)
        back(i)
        stack.pop()
back(1)
