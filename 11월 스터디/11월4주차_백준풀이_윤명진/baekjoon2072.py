import sys
input = sys.stdin.readline

def is_finish():
    for i in range(19):
        for j in range(19):
            # 빈칸은 건너뛰기
            if board[i][j] == 0:
                continue

            current_color = board[i][j]

            # 델타로 오른쪽, 아래, 오른쪽 아래 대각선, 오른쪽 위 대각선 탐색
            # 주의해야할 점은 육목 처리
            # 예를 들어 1 1 1 1 1 1을 생각해보자.
            # 첫번쨰 1에서는 육목 처리가 되지만,
            # 두번째 1부터는 오른쪽만 탐색하면 오목으로 처리되므로 주의
            # 즉, 반대방향도 체크해야함, 반대 방향에 같은 색 돌이 있을 경우
            # 이미 체크한 것이므로 다음 방향 탐색
            for di, dj in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                bi, bj = i - di, j - dj

                if (0 <= bi < 19 and 0 <= bj < 19) and board[bi][bj] == current_color:
                    continue

                cnt = 1

                for k in range(1, 19):
                    ni, nj = i + k * di, j + k * dj

                    # 범위를 벗어나거나 다른 색 돌을 만나면 탐색 중지
                    if not (0 <= ni < 19 and 0 <= nj < 19) or board[ni][nj] != current_color:
                        break

                    cnt += 1

                if cnt == 5:
                    return True

    # 모든 탐색이 끝났는데 오목이 없으면 False 반환
    return False


N = int(input())
board = [[0] * 19 for _ in range(19)]
current_turn = 0
is_possible = False

while current_turn < N:
    current_turn += 1
    si, sj = map(int, input().split())

    si -= 1
    sj -= 1

    # 흑차례 돌 놓기
    if current_turn % 2 == 1:
        board[si][sj] = 1
        
    # 백차례 돌 놓기
    else:
        board[si][sj] = 2

    # 오목이 끝났는지 체크
    if is_finish():
        print(current_turn)
        is_possible = True
        break

if not is_possible:
    print(-1)