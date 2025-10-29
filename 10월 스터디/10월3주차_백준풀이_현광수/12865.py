N, K = map(int, input().split())

# 무게를 기준으로 한 dp list 생성
dp = [0 for _ in range(K + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    for j in range(K, W - 1, -1):
        # K부터 W - 1R까지 순회 하면서
        # j에 들어가 있는 무게와 그 이전들에서 더해진 무게를 더했을 때를 비교하여
        # 최대값을 넣기
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[K])