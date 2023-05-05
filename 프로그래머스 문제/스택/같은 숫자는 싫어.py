def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        else:
            if arr[i] == answer[-1]:
                continue
            else:
                answer.append(arr[i])
    return answer