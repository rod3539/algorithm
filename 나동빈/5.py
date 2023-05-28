from itertools import permutations
def solution(N, arr, conditions):
    answer = 0
    for warriors in list(permutations(arr, N)):
        answer += 1
        for i in range(N-1):
            if conditions[i] == 1:
                if warriors[i] <= warriors[i+1]:
                    answer -= 1
                    break
            elif conditions[i] == 2:
                if warriors[i] >= warriors[i+1]:
                    answer -= 1
                    continue
            elif conditions[i] == 3:
                if warriors[i] != warriors[i+1]:
                    answer -= 1
                    break
    if answer < 0:
        answer = 0
    return answer