N = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

# 이 문제는 메모리가 4MB이므로 전체를 바로 리스트로 저장하면
# 메모리 초과 발생
# dp에 저장했으면 이전 최솟값들을 굳이 배열에 저장할 필요 없으므로
# 세 수를 입력받으면서 dp를 계속 갱신하기
for _ in range(N):
    a, b, c = map(int, input().split())

    # 왼쪽 끝
    left = max(max_dp[0] + a, max_dp[1] + a)

    # 가운데
    mid = max(max_dp[0] + b, max_dp[1] + b, max_dp[2] + b)

    # 오른쪽 끝
    right = max(max_dp[1] + c, max_dp[2] + c)

    max_dp[0], max_dp[1], max_dp[2] = left, mid, right


    # 왼쪽 끝
    left_min = min(min_dp[0] + a, min_dp[1] + a)

    # 가운데
    mid_min = min(min_dp[0] + b, min_dp[1] + b, min_dp[2] + b)

    # 오른쪽 끝
    right_min = min(min_dp[1] + c, min_dp[2] + c)

    min_dp[0], min_dp[1], min_dp[2] = left_min, mid_min, right_min


print(max(max_dp), min(min_dp))