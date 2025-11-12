import sys
input = sys.stdin.readline

# 연속된 가장 긴 사탕의 개수 찾는 함수
def check_max_candy(candies):
    global max_count

    for i in range(N):
        for j in range(N):
            current_color = candies[i][j]
            # 위에서부터 오른쪽 방향으로 탐색하므로, 델타를 오른쪽과 아래만 탐색
            for di, dj in [(0, 1), (1, 0)]:
                equal_cnt = 1
                for k in range(1, N):
                    ni, nj = i + k * di, j + k * dj
                    # 범위 벗어나면 다음 방향 탐색
                    if not (0 <= ni < N and 0 <= nj < N):
                        break

                    # 현재 사탕색과 다르면 다음 방향 탐색
                    if candies[ni][nj] != current_color:
                        break

                    if candies[ni][nj] == current_color:
                        equal_cnt += 1
                        max_count = max(max_count, equal_cnt)

N = int(input())

candy = [list(input().rstrip()) for _ in range(N)]
max_count = 0

for i in range(N):
    for j in range(N-1):
        # 오른쪽과 스왑해보기
        candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        check_max_candy(candy)
        # 원래대로 되돌리기
        candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

for i in range(N - 1):
    for j in range(N):
        # 아래쪽과 스왑해보기
        candy[i + 1][j], candy[i][j] = candy[i][j], candy[i + 1][j]
        check_max_candy(candy)
        # 원래대로 되돌리기
        candy[i + 1][j], candy[i][j] = candy[i][j], candy[i + 1][j]

print(max_count)