import sys
input = sys.stdin.readline

N = int(input())

dp = [[] for _ in range(N)]

# dp[i][j]는 길이가 i이면서 끝자리가 j인 계단수의 개수
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 생각해 보면 길이가 i이면서 0으로 끝나는 계단수는
# 길이가 i-1이면서 끝이 1로 끝나는 계단수로부터 만들 수 있음
# 예를 들어 길이가 3이면서 끝이 1로 끝나는 계단수는 321, 101뿐이므로
# 길이가 4이면서 끝이 0으로 끝나는 계단 수는 3210, 1010뿐임

# 2로 끝나는 계단 수는 전에 1로 끝나거나 3으로 끝나야 함.
# 마찬가지로 j(2~8)로 끝나는 계단 수는 전에 j-1로 끝나거나 j+1로 끝나야 함.
# 또, 9는 전에 8로 끝나야 함

# 이를 이용하여 dp 배열을 다음과 같이 만들 수 있음
for i in range(1, N):
    zero_cnt = dp[i-1][1] % 1000000000
    one_cnt = dp[i-1][0] + dp[i-1][2] % 1000000000
    two_cnt = dp[i-1][1] + dp[i-1][3] % 1000000000
    three_cnt = dp[i-1][2] + dp[i-1][4] % 1000000000
    four_cnt = dp[i-1][3] + dp[i-1][5] % 1000000000
    five_cnt = dp[i-1][4] + dp[i-1][6] % 1000000000
    six_cnt = dp[i-1][5] + dp[i-1][7] % 1000000000
    seven_cnt = dp[i-1][6] + dp[i-1][8] % 1000000000
    eight_cnt = dp[i-1][7] + dp[i-1][9] % 1000000000
    nine_cnt = dp[i-1][8] % 1000000000
    dp[i] = [zero_cnt, one_cnt, two_cnt, three_cnt, four_cnt, five_cnt, six_cnt, seven_cnt, eight_cnt, nine_cnt]

print(sum(dp[N-1]) % 1000000000)