import sys

n = int(sys.stdin.readline())

# 계단 점수 입력
stairs = [0] * (n + 1)
for i in range(1, n + 1):
    stairs[i] = int(sys.stdin.readline())

# dp에 각 계단까지의 최댓값 저장할 배열 생성
dp = [0] * (n + 1)

# 첫번째 계단의 최댓값은 stairs[1]
if n == 1:
    print(stairs[1])

# 두번째 계단의 최댓값은 stairs[1] + stairs[2]
elif n == 2:
    print(stairs[1] + stairs[2])

# 3번째 계단부터는 두가지 경우를 생각해야 함.
# 첫번째 경우: 전전 계단의 최댓값 점수 + 현재 계단의 점수
# 두번째 경우: 전전전 계단의 최댓값 점수 + 바로 직전 계단의 점수 + 현재 계단의 점수
# 둘 중 더 높은 점수가 최댓값

else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        # 전전계단의 최댓값 + 현재 계단
        
        case1 = dp[i - 2] + stairs[i]

        # 전전전계단의 최댓값 + 전 계단의 최댓값 + 현재 계단
        case2 = dp[i - 3] + stairs[i - 1] + stairs[i]

        # 둘 중 더 큰 값이 최댓값임
        dp[i] = max(case1, case2)

    print(dp[n])