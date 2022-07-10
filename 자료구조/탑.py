N = int(input())
buildings = list(map(int, input().split()))
result = [0] * N
for i, building in enumerate(buildings):
    for j in range(i+1, N):
        if buildings[j] < building:
            result[j] = i + 1
        else:
            break
print(*result)
