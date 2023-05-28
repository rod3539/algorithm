def solution(N):
    answer = 0
    for i in range(1, N + 1):
        answer += str(i).count('3')
        answer += str(i).count('7')
    return answer