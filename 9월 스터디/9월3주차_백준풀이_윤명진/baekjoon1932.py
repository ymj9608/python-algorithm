import sys
input = sys.stdin.readline

N = int(input())
triangles = [list(map(int, input().split())) for _ in range(N)]

# 정수 삼각형 모양에 맞게 dp를 이차원 배열로 생성
dp = [[0] * i for i in range(1, N + 1)]

# 1층이면 그냥 출력하면 됨
if N == 1:
    print(triangles[0][0])

# 2층 이상일 경우
else:
    dp[0][0] = triangles[0][0]
    dp[1][0] = triangles[0][0] + triangles[1][0]
    dp[1][1] = triangles[0][0] + triangles[1][1]


    for i in range(2, N):
        for j in range(i + 1):
            # i번째 층의 왼쪽 끝의 최댓값
            dp[i][0] = dp[i-1][0] + triangles[i][0]

            # i번째 층의 오른쪽 끝의 최댓값
            dp[i][-1] = dp[i-1][-1] + triangles[i][-1]

            # 나머지는 전층의 왼쪽, 오른쪽 중 더 큰 값을 선택
            if 0 < j < i:
                prev_sum = max(dp[i-1][j - 1], dp[i-1][j])
                dp[i][j] = prev_sum + triangles[i][j]

    print(max(dp[N - 1]))

