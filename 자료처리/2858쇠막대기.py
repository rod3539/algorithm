arr = list(input())
stick = 0
count = 0
i = 0
while i < len(arr):
    if arr[i] == '(' and arr[i + 1] == ')':
        count += stick
        i += 2
    elif arr[i] == '(':
        stick += 1
        i += 1
    else:
        count += 1
        stick -= 1
        i += 1
print(count)