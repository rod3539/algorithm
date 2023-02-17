import heapq

def solution(operations):
    queue = []
    for operation in operations:
        o, d = operation.split()
        if o == 'I':
            heapq.heappush(queue, int(d))
        elif o == 'D' and d == '-1':
            heapq.heappop(queue)
        elif o == 'D' and d == '1':
            if queue:
                queue.remove(max(queue))
    if not queue:
        return [0, 0]
    return max(queue), queue[0]