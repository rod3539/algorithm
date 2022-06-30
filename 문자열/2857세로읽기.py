arr = []
answer = []
max_num = 0

for _ in range(5):
    string = input()
    if max_num < len(string):
        max_num = len(string)
    arr.append(list(string))
for i in range(max_num):
    for j in range(5):
        if i < len(arr[j]):
            answer.append(arr[j][i])
print(''.join(answer))