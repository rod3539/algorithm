n, m = map(int, input().split())
stack = []
def back():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(1, n + 1):
        stack.append(i)
        back()
        stack.pop()
back()
