# 빙고보드와 심판이 부르는 숫자
board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]

# 지우는 것 표시
# 첫 줄은 세로, 우하향 대각선
# 두 번째 줄은 가로, 좌상향 대각선
bingo = [[0] * 6 for _ in range(2)]
# 몇 번째 숫자인지
count = 0
# 빙고 한 거 중복제거로 담기
finish = set()

# 심판이 부르는 것부터 순회
for i in range(5):
    for j in range(5):
        number = numbers[i][j]
        count += 1
        # 숫자 찾았는지 확인하는 플래그
        find = 0
        # 보드판 탐색
        for r in range(5):
            for c in range(5):
                # 심판 숫자와 같은 숫자 찾으면
                if board[r][c] == number:
                    # 세로줄 체크, 중복 체크 안 하면 빙고가 많아지는 것처럼 보임
                    bingo[0][c] += 1
                    if bingo[0][c] == 5 and ('col', c) not in finish:
                        finish.add(('col', c))

                    # 가로줄 체크
                    bingo[1][r] += 1
                    if bingo[1][r] == 5 and ('row', r) not in finish:
                        finish.add(('row', r))

                    # 우하향 대각선 체크
                    if r == c:
                        bingo[0][5] += 1
                        if bingo[0][5] == 5 and ('right', 5) not in finish:
                            finish.add(('right', 5))

                    # 좌상향 대각선 체크
                    if r + c == 4:
                        bingo[1][5] += 1
                        if bingo[1][5] == 5 and ('left', 5) not in finish:
                            finish.add(('left', 5))

                    # 찾은 숫자 체크해주고 for문 나가기
                    find = 1
                    break
            # 플래그 확인
            if find == 1:
                break

        # 빙고 3개 됐으면 출력하고 나가기
        if len(finish) >= 3:
            print(count)
            break

    if len(finish) >= 3:
        break

# 빙고 중복 체크 문제로 인해 틀렸었음