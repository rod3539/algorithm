result = []
messages = []
while True:
    words = input().split()
    if words[0] == 'END':
        break
    for word in words:
        if word not in messages:
            messages.append(word)
    result.append(' '.join(messages))
for z in result:
    print(z)