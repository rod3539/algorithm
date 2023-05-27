def solution(N, warriors):
    answer = 0
    # 자신감 점수를 계속 구해야 하므로 함수로 만들어서 재사용
    def confidence(warrior):
        # 자신감 점수
        count = 0
        # 첫 번째 전사와 마지막 전사는 따로 확인해준다
        if warrior[0] > warrior[1] and warrior[0] > warrior[-1]:
            count += 1
        if warrior[-1] > warrior[0] and warrior[-1] > warrior[-2]:
            count += 1
        # 그 외의 전사들은 for문을 돌면서 옆에 있는 전사들과 전투력을 비교한다.
        for i in range(1, len(warrior)-1):
            if warrior[i] > warrior[i-1] and warrior[i] > warrior[i+1]:
                count += 1
        return count
    # warriors 리스트를 슬라이싱을 활용해 복사
    warrior = warriors[:]
    for ii in range(N):
        # 원소들을 하나씩 빼준다
        warrior.pop(ii)
        # 자신감 점수를 구하는 함수 호출
        score = confidence(warrior)
        # 만약 자신감 점수가 answer보다 크다면 answer 갱신
        if score > answer:
            answer = score
        # 다시 warriors 리스트 원상 복구
        warrior = warriors[:]
    return answer

print(solution(8, [7, 7, 5, 8, 9, 4, 6, 2]))
print(solution(10, [5, 3, 7, 5, 3, 3, 6, 1, 8, 7]))
print(solution(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
