for tc in range(1, 11):
    T = int(input())
    s = input()
    sens = input()

    answer = sens.count(s)
    print(f'#{tc} {answer}')