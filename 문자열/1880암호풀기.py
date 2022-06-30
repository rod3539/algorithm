key = input()
message = input()
alpha = ''
for i in range(97, 123):
    alpha += chr(i)
result = ''
for i in range(len(message)):
    if message[i] == ' ':
        result += ' '
    else:
        if message[i].isupper():
            for j in range(26):
                if message[i].lower() == alpha[j]:
                    result += key[j].upper()
        else:
            for j in range(26):
                if message[i] == alpha[j]:
                    result += key[j]
print(result)