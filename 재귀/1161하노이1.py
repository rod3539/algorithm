def hanoi(n, first, sec, thr):
    if n == 1:
        print(f'{n} : {first} -> {thr}')
        return
    else:
        hanoi(n-1, first, thr, sec)
        print(f'{n} : {first} -> {thr}')
        hanoi(n-1, sec, first, thr)

n = int(input())
hanoi(n, 1, 2, 3)