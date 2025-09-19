# 색종이 만들기(어려움,,)
import sys
input = sys.stdin.readline

def four_divide(li, size):
    global total_blue_count, total_white_count
    b_count = 0
    w_count = 0

    for row in range(size):
        b_count += li[row].count(1)
        w_count += li[row].count(0)

    # 전부다 파란색이라면
    if b_count == size ** 2:
        total_blue_count += 1

    # 전부다 하얀색이라면
    elif w_count == size ** 2:
        total_white_count += 1

    # 그 이외의 경우는 4분할하기
    else:
        # 2사분면 row: 0~N/2
        first_li = []

        for row in (N/2):
            first_li.append(li[row][0:N/2])

        four_divide(first_li, size/2)

        # 1사분면
        second_li = []

        for row in (N / 2):
            second_li.append(li[row][N / 2:])

        four_divide(second_li, size/2)

        # 3사분면
        third_li = []

        for row in (N // 2 + 1, N):
            third_li.append(li[row][:N // 2])

        four_divide(third_li, size//2)

        # 4사분면
        fourth_li = []

        for row in (N // 2 + 1, N):
            third_li.append(li[row][N // 2:])

        four_divide(fourth_li, size // 2)

N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

total_blue_count = 0
total_white_count = 0

print(total_white_count, total_blue_count)