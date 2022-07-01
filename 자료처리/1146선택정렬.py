n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)