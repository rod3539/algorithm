def solution(k, tangerine):
    answer = 0
    dic = {}

    for i in set(tangerine):
        dic[i] = 0

    for t in tangerine:
        dic[t] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for key, value in dic:
        k = k - value
        answer += 1
        if k <= 0:
            break
    return answer