def solution(brown, yellow):
    answer = []
    divList = []
    n = brown + yellow

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divList.append(i)
            if (i ** 2) != n:
                divList.append(n // i)

    for i in range(0, len(divList) - 1, 2):
        if ((divList[i] - 2) * 2) + (divList[i + 1] * 2) == brown:
            answer.append(divList[i + 1])
            answer.append(divList[i])
            break

    if not answer:
        answer.append(divList[-1])
        answer.append(divList[-1])

    return answer