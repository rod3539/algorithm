n = int(input())
money = 1000 - n
answer = 0
changes = [500, 100, 50, 10, 5, 1]

for change in changes:
    if money == 0:
        break
    answer += money // change
    money = money % change
print(answer)