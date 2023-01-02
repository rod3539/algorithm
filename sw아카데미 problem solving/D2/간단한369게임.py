N = int(input())
arr = []
for i in range(1, N + 1):
    count = 0
    for j in range(len(str(i))):
        if str(i)[j] in '3':
            count += 1
        elif str(i)[j] in '6':
            count += 1
        elif str(i)[j] in '9':
            count += 1
    if count == 1:
        arr.append('-')
    elif count == 2:
        arr.append('--')
    elif count == 3:
        arr.append('---')
    else:
        arr.append(str(i))
print(' '.join(arr))
