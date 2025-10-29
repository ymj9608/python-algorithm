N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N + 1)]

dp[1][0] = 1   # 아무것도 안 둠
dp[1][1] = 1   # 위쪽에 사자
dp[1][2] = 1   # 아래쪽에 사자

for i in range(2, N + 1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

answer = (dp[N][0] + dp[N][1] + dp[N][2]) % 9901

print(dp)
print(answer)