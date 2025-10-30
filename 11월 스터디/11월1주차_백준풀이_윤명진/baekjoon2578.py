import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
is_bingo = False
while True:
    num_list = list(map(int, input().split()))

    for num in num_list:
        bingo_count = 0
        is_end = False
        for i in range(5):
            for j in range(5):
                # 부른 숫자 지우기
                if bingo[i][j] == num:
                    bingo[i][j] = 0
                    cnt += 1
                    is_end = True
                    break
            if is_end:
                break

        # 수를 지웠으면 빙고가 3개 됐는지 체크 (행, 열, 대각선)

        # 행 체크
        for i in range(5):
            if bingo[i].count(0) == 5:
                bingo_count += 1

        # 열 체크
        for i in range(5):
            zero_count = 0
            for j in range(5):
                if bingo[j][i] == 0:
                    zero_count += 1

            if zero_count == 5:
                bingo_count += 1

        # 대각선 체크
        zero_count = 0
        for i in range(5):
            if bingo[i][i] == 0:
                zero_count += 1

            if zero_count == 5:
                bingo_count += 1

        zero_count = 0
        for i in range(5):
            if bingo[i][4 - i] == 0:
                zero_count += 1

            if zero_count == 5:
                bingo_count += 1

        if bingo_count >= 3:
            print(cnt)
            is_bingo = True
            break

    if is_bingo:
        break