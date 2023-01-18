def solution(n):
    answer = 0
    num = bin(n)[2:].count('1')
    for i in range(n+1, 1000001):
        if bin(i)[2:].count('1') == num:
            answer = i
            break
    return answer