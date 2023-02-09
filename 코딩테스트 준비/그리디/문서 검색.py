
sentence = input()
search = input()

# print(sentence.count(search))
answer = 0
while True:
    i = sentence.find(search)
    if i == -1:
        break
    answer += 1
    sentence = sentence[i+len(search):]
print(answer)