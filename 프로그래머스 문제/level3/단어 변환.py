from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, 0))
    n = len(words)
    visited = [0] * n
    while queue:
        word, count = queue.popleft()
        if word == target:
            answer = count
            break
        for i in range(n):
            idx = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        idx += 1
                if idx == 1:
                    queue.append((words[i], count + 1))
                    visited[i] = 1

    return answer