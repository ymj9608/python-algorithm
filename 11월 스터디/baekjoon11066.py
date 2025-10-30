import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    files = list(map(int, input().split()))

    # subtotal[i] = files[0]부터 files[i-1]까지의 합
    subtotal = [0] * (N + 1)
    for i in range(1, N + 1):
        subtotal[i] = subtotal[i - 1] + files[i - 1]

    # dp[i][j]: i번째 파일부터 j번째 파일까지 합치는 최소 비용
    dp = [[float('inf')] * N for _ in range(N)]

    # opt_k[i][j]: dp[i][j]를 최소로 만드는 분할 지점 k
    opt_k = [[0] * N for _ in range(N)]

    # 길이가 1인 경우
    for i in range(N):
        dp[i][i] = 0
        opt_k[i][i] = i

    # 합치는 파일의 길이 (2부터 N까지)
    for length in range(2, N + 1):
        # j: 시작 파일 인덱스
        for j in range(N - length + 1):
            # end: 끝 파일 인덱스
            end = j + length - 1

            # 현재 구간 [j, end]를 합치는 비용 (마지막에 한 번 더해짐)
            cost = subtotal[end + 1] - subtotal[j]

            k_start = opt_k[j][end - 1]
            k_end = opt_k[j + 1][end]

            # k는 [j, end-1] 범위를 넘을 수 없음
            for k in range(k_start, min(end, k_end + 1)):
                current_cost = dp[j][k] + dp[k + 1][end]

                if current_cost < dp[j][end]:
                    dp[j][end] = current_cost
                    opt_k[j][end] = k

            dp[j][end] += cost

    print(dp[0][N - 1])