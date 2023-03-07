n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i-1] + 1
    if not i % 2:
        d[i] = min(d[i], d[i // 2] + 1)
    if not i % 3:
        d[i] = min(d[i], d[i // 3] + 1)
print(d[n])