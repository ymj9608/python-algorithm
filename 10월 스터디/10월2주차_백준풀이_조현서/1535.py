# 안녕
'''
dp 문제(어려움...)
'''
import sys
input = sys.stdin.readline

N = int(input())
# 인덱스와 사람 번호와 맞추기 위함
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0] * 100 for _ in range(N + 1)]

for i in range(1, N + 1):
    for hp in range(100):
        # i번째 사람을 고르지 않으면 체력은 전 사람꺼 그대로 유지
        dp[i][hp] = dp[i-1][hp]

        # 골랐을 경우
        if hp - L[i] >= 0:
            val = dp[i-1][hp - L[i]] + J[i]
            if val > dp[i][hp]:
                dp[i][hp] = val

print(max(dp[N]))