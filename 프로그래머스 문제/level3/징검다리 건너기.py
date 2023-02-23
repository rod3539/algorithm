def solution(stones, k):
    answer = 0
    count = 0

    while count < k:
        count = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                count += 1
                if count >= k:
                    break
                continue
            else:
                stones[i] -= 1
                count = 0
        if count >= k:
            break
        answer += 1
    return answer
