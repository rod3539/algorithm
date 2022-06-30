s = input()
KOI = 0
IOI = 0
for i in range(len(s) - 2):
    part = s[i] + s[i+1] + s[i+2]
    if part == 'KOI':
        KOI += 1
    elif part == 'IOI':
        IOI += 1
print(KOI)
print(IOI)
