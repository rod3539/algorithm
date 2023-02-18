from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)

    return answer