import sys

input = sys.stdin.readline()

n = int(input)

if n == 1 or n == 3:
    print(-1)
elif n % 5 == 1 or n % 5 == 3:
    a = n // 5 - 1
    b = (n - a * 5) // 2
    print(a + b)
elif n % 5 == 2 or n % 5 == 4:
    a = n // 5
    b = (n - a * 5) // 2
    print(a + b)
else:
    print(n // 5)
