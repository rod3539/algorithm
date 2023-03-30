from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((0, begin))
    while queue:
        idx, now = queue.popleft()
        if now == target:
            answer = idx
            break
        if idx > len(words):
            break
        for word in words:
            count = 0



    return answer