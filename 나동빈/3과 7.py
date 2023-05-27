def solution(N):
    answer = 0
    # 1부터 N까지 숫자들을 모두 순회하면서 각 숫자들이 3과 7을 몇 개나 가지고 있는지 확인한다.
    for i in range(1, N + 1):
        # 숫자를 str으로 변환 후 확인
        answer += str(i).count('3')
        answer += str(i).count('7')
    return answer

print(solution(37))
print(solution(100))
print(solution(88888))