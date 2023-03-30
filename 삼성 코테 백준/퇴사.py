import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    # i 일에 퇴사일 넘기는 경우
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # i일에 상담 하는 것과 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])