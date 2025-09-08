N = int(input())

my_list = [list(map(int, input().split())) for _ in range(N)]

# 빨, 초, 파 각각 최댓값을 저장하기 위한 배열 생성
dp = [[0, 0, 0] for _ in range(N)]

dp[0] = my_list[0]


# 지금 집을 빨간색으로 칠한 경우는 이전 집을 파란색 또는 초록색으로 칠한 경우의 합을 계산하고 그중 최솟값 찾기
dp[1][0] = min(dp[0][1] + my_list[1][0], dp[0][2] + my_list[1][0])
dp[1][1] = min(dp[0][0] + my_list[1][1], dp[0][2] + my_list[1][1])
dp[1][2] = min(dp[0][0] + my_list[1][2], dp[0][1] + my_list[1][2])

# i번째 집을 빨간색으로 칠한 경우는 i - 1번째 집을 파란색 또는 초록색으로 칠한 경우의 합을 계산하고 그중 최솟값 찾기
for i in range(2, N):
    dp[i][0] = min(dp[i-1][1] + my_list[i][0], dp[i-1][2] + my_list[i][0])
    dp[i][1] = min(dp[i-1][0] + my_list[i][1], dp[i-1][2] + my_list[i][1])
    dp[i][2] = min(dp[i-1][0] + my_list[i][2], dp[i-1][1] + my_list[i][2])

print(min(dp[N-1]))