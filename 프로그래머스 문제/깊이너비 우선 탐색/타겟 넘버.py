from collections import deque
def solution(numbers, target):
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-1 * numbers[0], 0))
    answer = 0
    while queue:
        now, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append((now + numbers[idx], idx))
            queue.append((now - numbers[idx], idx))
        else:
            if now == target:
                answer += 1
    return answer