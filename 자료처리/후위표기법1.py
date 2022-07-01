n = int(input())
num_list = list(input().split())
stack = []
opp = ['+', '-', '*', '/']

for num in num_list:
    if num in opp:
        if num == '+':
            stack.append(stack.pop() + stack.pop())
        elif num == '-':
            A, B = stack.pop(), stack.pop()
            stack.append(B - A)
        elif num == '*':
            stack.append(stack.pop() * stack.pop())
        elif num == '/':
            A, B = stack.pop(), stack.pop()
            stack.append(B // A)
    else:
        stack.append(int(num))
print(int(stack[0]))