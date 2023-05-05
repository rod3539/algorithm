from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    answer = 1
    for c in clothes:
        dic[c[1]] += 1
    for value in dic.values():
        answer *= value+1
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))