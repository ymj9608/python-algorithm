N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]
answer = 0

for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][1]
        elif j == 9:
            dp[i][9] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

for i in range(10):
    answer += dp[N - 1][i]

print(answer % 1000000000)