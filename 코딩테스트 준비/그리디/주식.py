for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    arr_max = 0
    for i in range(n-1, -1, -1):
        if arr[i] > arr_max:
            arr_max = arr[i]
        else:
            answer += arr_max - arr[i]
    print(answer)