from collections import deque
a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))

while queue:
    x, t = queue.popleft()
    if x == b:
        print(t)
        exit()
    if x * 2 <= b:
        queue.append((x*2, t + 1))
    x = int(str(x) + '1')
    if x <= b:
        queue.append((x, t + 1))
print(-1)
