from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([-1 * numbers[0], 0])
    queue.append([numbers[0], 0])
    n = len(numbers)
    while queue:
        now, i = queue.popleft()
        i += 1
        if i < n:
            queue.append([now + numbers[i], i])
            queue.append([now - numbers[i], i])
        else:
            if now == target:
                answer += 1

    return answer
