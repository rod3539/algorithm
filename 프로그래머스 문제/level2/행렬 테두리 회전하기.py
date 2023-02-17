from collections import deque
def solution(rows, columns, queries):
    answer = []
    if len(queries) == 1:
        answer.append(min(queries[0]))
        return answer

    arr = [[0] * columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] += count
            count += 1

    for querie in queries:
        x1, y1, x2, y2 = querie[0]-1, querie[1]-1, querie[2]-1, querie[3]-1
        q = deque()
        for i in range(y1, y2):
            q.append(arr[x1][i])
        for i in range(x1, x2):
            q.append(arr[i][y2])
        for i in range(y2, y1, -1):
            q.append(arr[x2][i])
        for i in range(x2, x1, -1):
            q.append(arr[i][y1])
        answer.append(min(q))

        for i in range(y1 + 1, y2+1):
            arr[x1][i] = q.popleft()
        for i in range(x1+1, x2+1):
            arr[i][y2] = q.popleft()
        for i in range(y2-1, y1-1, -1):
            arr[x2][i] = q.popleft()
        for i in range(x2-1, x1-1, -1):
            arr[i][y1] = q.popleft()

    return answer

# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))