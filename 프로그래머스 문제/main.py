import heapq
def solution(scoville, K):
    if min(scoville) >= K:
        return 0
    answer = 0
    heapq.heapify(scoville)
    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        c = a + b * 2
        heapq.heappush(scoville, c)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer