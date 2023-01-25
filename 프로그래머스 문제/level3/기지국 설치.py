import math


def solution(n, stations, w):
    answer = 0
    dist = []  # 전파 전달 안되는 구간 길이 저장할 리스트
    for i in range(1, len(stations)):
        dist.append((stations[i] - w - 1) - (stations[i - 1] + w))

    dist.append(stations[0] - w - 1)  # 맨앞
    dist.append(n - (stations[-1] + w))  # 맨뒤

    for i in dist:
        if i <= 0:
            continue
        else:
            answer += math.ceil(i / (2 * w + 1))  # 올림
    return answer