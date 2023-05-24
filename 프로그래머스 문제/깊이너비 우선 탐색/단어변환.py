from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    queue = deque()
    queue.append((begin, 0))
    while queue:
        now, idx = queue.popleft()
        if idx > len(words):
            return 0
        if now == target:
            return idx
        for word in words:
            count = 0
            for i in range(len(word)):
                if count > 2:
                    break
                if word[i] != now[i]:
                    count += 1
            if count == 1:
                queue.append((word, idx + 1))
