import sys
input = sys.stdin.readline
for _ in range(int(input())):
    r, sen = map(str, input().split())
    answer = ''
    for s in sen:
        answer += s * int(r)
    print(answer)
