N = int(input())

for i in range(1, 2 ** 32):
    if i ** 2 > N:
        print(i - 1)
        break