import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

dp = [1] * N

# dp[i]의 값은 i번째 값을 포함하는 가장 긴 수열의 길이가 저장됨
for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))