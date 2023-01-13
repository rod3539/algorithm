from collections import deque
for tc in range(10):
    T = int(input())
    arr = deque(list(map(int, input().split())))
    answer = []
    while arr[-1]:
        for i in range(1, 6):
            if arr[0] - i <= 0:
                arr.popleft()
                arr.append(0)
                break
            else:
                arr.append(arr[0] - i)
                arr.popleft()
    print(f'#{T}', end=' ')            
    print(*arr)

