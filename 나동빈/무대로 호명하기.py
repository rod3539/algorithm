# 부른 학생이 서있는 위치를 먼저 찾는다.

def solution(N, students, calls):
    answer = 0
    # 학생을 calls 만큼 부르니까 calls배열을 모두 순회한다.
    for call in calls:
        # 부른 학생이 서있는 위치를 먼저 찾는다.
        count = students.index(call)
        # 학생의 위치만큼이 학생이 무대로 올라가는데 걸리는 시간이므로 answer에 더해준다.
        answer += count
        # students 배열에서 그 학생이 서있던 곳을 빼준다.
        students.pop(count)
    return answer

print(solution(8, [7, 3, 5, 1, 8, 6, 4, 2], [1, 2, 3, 4, 5, 6, 7, 8]))
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution(10,[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution(10, [7, 3, 2, 5, 1, 6, 8, 9, 10, 4], [9, 2, 1, 5, 4, 6, 8, 10, 3, 7]))