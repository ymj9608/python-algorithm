# 가장 긴 증가하는 부분 수열
'''
수열 A가 주어지면 증가하는 부분에 해당하는
수열의 길이를 구함
명진님이 dp로 푸는 걸 추천하심
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
