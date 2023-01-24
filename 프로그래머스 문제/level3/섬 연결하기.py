def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    arr = set([costs[0][0]])
    while len(arr) < n:
        for cost in costs:
            if cost[0] in arr and cost[1] in arr:
                continue
            if cost[0] in arr or cost[1] in arr:
                arr.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer