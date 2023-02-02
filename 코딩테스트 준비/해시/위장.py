
def solution(clothes):
    answer = 1
    dic = dict()
    for cloth in clothes:
        dic[cloth[1]] = dic.get(cloth[1], 0) + 1
    for type in dic:
        answer += (dic[type] + 1)
    return answer - 1