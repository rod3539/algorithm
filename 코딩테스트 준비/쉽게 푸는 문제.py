A, B = map(int, input().split())
result = 0
sumA = 0
arr = []
for i in range(1, 1001):
    count = 1
    if result >= 1000:
        break
    while i >= count:
        arr.append(i)
        count += 1
        result += 1
for i in range(A-1, B):
    sumA += arr[i]
print(sumA)