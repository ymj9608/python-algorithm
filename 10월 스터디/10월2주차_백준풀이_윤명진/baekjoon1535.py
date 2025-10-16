import sys
input = sys.stdin.readline

N = int(input())

# 아이디어 (배낭 문제)
# dp[i][j]는 i번째 사람까지 인사를 주고 받았을 때 (1~i번째 사람 각각 인사를 안했을 수도 있음), j만큼의 체력이 남았다는 뜻

loss_hp = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if j >= loss_hp[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - loss_hp[i]] + happiness[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N])
# HP가 100이 되면 죽으므로 HP가 1 남았을 때가 최댓값임 즉, dp[N][99]
print(dp[N][99])