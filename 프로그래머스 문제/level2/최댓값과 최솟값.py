def solution(s):
    answer = ''
    nums = s.split(' ')
    max_n = float('-inf')
    min_n = float('inf')
    for num in nums:
        if int(num) > max_n:
            max_n = int(num)
        if int(num) < min_n:
            min_n = int(num)
    answer = str(min_n) + ' ' + str(max_n)

    return answer
