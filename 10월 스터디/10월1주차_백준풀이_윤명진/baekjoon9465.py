import sys
input = sys.stdin.readline

T = int(input())

for case in range(T):
    n = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        
    else:
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]

        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

        # 세번째부터는 뗼지 안뗄지 선택
        # 이때 dp[0][i]가 될 수 있는 후보들은 아래 두 가지 경우임
        # 첫번째 케이스: max(dp[0][i-2], dp[1][i-2]) + stickers[0][i]
        # 두번째 케이스: dp[1][i-1] + stickers[0][i]

        # 마찬가지로 dp[1][i]가 될 수 있는 후보들은 아래 두 가지 경우임
        # 첫번째 케이스: max(dp[0][i-2], dp[1][i-2]) + stickers[1][i]
        # 두번째 케이스: dp[0][i-1] + stickers[1][i]
        for i in range(2, n):
            case1 = max(dp[0][i-2], dp[1][i-2]) + stickers[0][i]
            case2 = dp[1][i-1] + stickers[0][i]
            dp[0][i] = max(case1, case2)

            case3 = max(dp[0][i-2], dp[1][i-2]) + stickers[1][i]
            case4 = dp[0][i-1] + stickers[1][i]
            dp[1][i] = max(case3, case4)

        print(max(dp[0][n-1], dp[1][n-1]))