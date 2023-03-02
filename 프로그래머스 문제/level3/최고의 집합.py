def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    num = s // n
    for _ in range(n):
        answer.append(num)
    idx = len(answer) - 1
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1

    return answer