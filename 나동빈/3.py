def solution(N, warriors):
    answer = 0
    def confidence(warrior):
        count = 0
        if warrior[0] > warrior[1] and warrior[0] > warrior[-1]:
            count += 1
        if warrior[-1] > warrior[0] and warrior[-1] > warrior[-2]:
            count += 1
        for i in range(1, len(warrior)-1):
            if warrior[i] > warrior[i-1] and warrior[i] > warrior[i+1]:
                count += 1
        return count
    warrior = warriors[:]
    for ii in range(N):
        warrior.pop(ii)
        score = confidence(warrior)
        if score > answer:
            answer = score
        warrior = warriors[:]
    return answer
