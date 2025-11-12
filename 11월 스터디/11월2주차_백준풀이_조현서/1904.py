# 01타일
'''
1과 00 2개의 타일이 있음
1 -> 2 -> 3 -> 5 -> 8,,,
피보나치 수열 형태
'''
import sys
input = sys.stdin.readline

N = int(input())

# '1'만 가능
if N == 1:
    print(1)

# '11'과 '00' 가능
elif N == 2:
    print(2)

else:
    dp = [[0] for _ in range(N)]
    dp[0] = 1 
    dp[1] = 2

    for i in range(2, N):
        dp[i] =(dp[i - 1] + dp[i - 2]) % 15746

    print(dp[N - 1])