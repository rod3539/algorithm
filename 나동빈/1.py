def solution(N, students, calls):
    answer = 0
    for call in calls:
        count = students.index(call)
        answer += count
        students.pop(count)
    return answer