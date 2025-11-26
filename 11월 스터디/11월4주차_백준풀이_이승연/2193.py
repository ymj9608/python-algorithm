import sys
input = sys.stdin.readline
N = int(input())

# 1 <= N <= 90이니까
dp = [0] * 91
dp[0] = dp[1] = 1

if N < 3:
    print(dp[N-1])
else:
    for i in range(N-2):
        # 1 / 10 / 100, 101 / 1000, 1001, 1010 / ... 로 찾은 DP 규칙
        dp[i+2] = dp[i+1] + dp[i]
    print(dp[N-1])