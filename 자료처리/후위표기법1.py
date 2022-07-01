n = int(input())
num_list = list(input().split())
stack = []

for num in num_list:
    if num == '+':
        A = stack.pop()
        B = stack.pop()
        num = A + B
        stack.append(num)
    elif num == '-':
        A = stack.pop()
        B = stack.pop()
        num = A - B
        stack.append(num)
    elif num == '*':
        A = stack.pop()
        B = stack.pop()
        num = A * B
        stack.append(num)
    elif num == '/':
        A = stack.pop()
        B = stack.pop()
        num = B // A
        stack.append(num)
    else:
        stack.append(int(num))
print(int(stack[0]))