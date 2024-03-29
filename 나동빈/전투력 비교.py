# permutations 활용 방법
from itertools import permutations
def solution(N, arr, conditions):
    answer = 0
    # permutations를 통해 완전 탐색
    for warriors in list(permutations(arr, N)):
        answer += 1
        for i in range(N-1):
            # 1이 경우에 왼쪽이 더 커야하므로
            if conditions[i] == 1:
                if warriors[i] <= warriors[i+1]:
                    answer -= 1
                    break
            # 2인 경우 오른쪽이 더 커야하므로
            elif conditions[i] == 2:
                if warriors[i] >= warriors[i+1]:
                    answer -= 1
                    continue
            # 3인 경우에는 같아야 하므로
            elif conditions[i] == 3:
                if warriors[i] != warriors[i+1]:
                    answer -= 1
                    break
    if answer < 0:
        answer = 0
    return answer


print(solution(5, [7, 10, 7, 5, 3], [3, 1, 2, 4]))
print(solution(3, [4, 5, 6], [1, 2]))