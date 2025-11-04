# 평범한 배낭
'''
안녕 문제(체력, 행복)과 거의 동일한 문제
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# dp 배열
dp = [0] * (K + 1)

for _ in range(N):
    weight, value = map(int, input().split())
    
    # 버틸 수 있는 무게에서 역으로 내려가기
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
        # print(dp)

print(dp[K])