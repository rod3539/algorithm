from collections import deque
a, b = map(int, input().split())
answer = 0
queue = deque()
queue.append([a, 0])
queue.append([a, 0])
while queue:
    now, idx = queue.popleft()
    if now == b:
        answer = idx
        break
    elif now > b:
        continue
    queue.append([now * 2, idx + 1])
    queue.append([now * 10 + 1, idx + 1])
if not answer:
    print(-1)
    exit()
print(answer + 1)