T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    num = []

    for i in range(len(arr)):
        if arr[i].isdigit():
            num.append(int(arr[i]))
        if arr[i] == '.':
            if len(num) != 1:
                print(f'#{tc} error')
                break
            print(f'#{tc} {num.pop()}')
            break
        if arr[i] == '+':
            if len(num) == 1 or len(num) == 0:
                print(f'#{tc} error')
                break
            num.append(num.pop(-2) + num.pop(-1))
        elif arr[i] == '-':
            if len(num) == 1 or len(num) == 0:
                print(f'#{tc} error')
                break
            num.append(num.pop(-2) - num.pop(-1))
        elif arr[i] == '*':
            if len(num) == 1 or len(num) == 0:
                print(f'#{tc} error')
                break
            num.append(num.pop(-2) * num.pop(-1))
        elif arr[i] == '/':
            if len(num) == 1 or len(num) == 0:
                print(f'#{tc} error')
                break
            num.append(num.pop(-2) // num.pop(-1))