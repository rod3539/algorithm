bowl = list(input())
height = 10
for i in range (1, len(bowl)):
    if bowl[i] == bowl[i - 1]:
        height += 5
    elif bowl[i] != bowl[i - 1]:
        height += 10
    else:
        print("Err")
print(height)
