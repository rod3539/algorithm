def dfs(depth, total, plus, minus, multiply, divide):
    global num_max, num_min
    if depth == N:
        num_max = max(total, num_max)
        num_min = min(total, num_min)
        return
    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)


N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

num_max = float('-inf')
num_min = float('inf')
dfs(1, numbers[0], operator[0], operator[1], operator[2], operator[3])
print(num_max)
print(num_min)

