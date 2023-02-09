n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(n-2):
    if arr[i+1] > arr[i+2]:
        m = min(arr[i], arr[i+1] - arr[i+2])
        answer += m * 5
        arr[i] -= m
        arr[i+1] -= m
    if arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
        m = min(arr[i], arr[i+1])
        answer += m * 7
        arr[i] -= m
        arr[i+1] -= m
        arr[i+2] -= m
    if arr[i] > 0:
        answer += arr[i] * 3

if arr[-2] > 0 and arr[-1] > 0:
    m = min(arr[-2], arr[-1])
    answer += (m * 5)
    arr[-2] -= m
    arr[-1] -= m

if arr[-2] > 0:
    answer += (arr[-2] * 3)
else:
    answer += (arr[-1] * 3)

print(answer)