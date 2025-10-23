N = int(input())

dp = [0] * 100

L = list(map(int, input().split()))
J = list(map(int, input().split()))

for i in range(N):
    for j in range(99, L[i] - 1, -1):
        cost = L[i]
        joy = J[i]
        dp[j] = max(dp[j], dp[j - cost] + joy)

print(dp[99])