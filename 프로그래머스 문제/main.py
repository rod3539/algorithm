def solution(data, n): 
    # Your code here
    a = set(data)
    answer = ''
    for i in a:
        if data.count(i) == n:
            answer += str(i) + ' '
    return answer[0:-1]

print(solution([1, 2, 3], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))