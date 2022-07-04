def my_factorial(n):
    if n > 1:
        return n * my_factorial(n-1)
    else:
        return 1

n = int(input())
for i in range(n, 0, -1):
    if i == 1:
        print('1! = 1')
    else:
        print(f'{i}! = {i} * {i - 1}!')
print(my_factorial(n))
