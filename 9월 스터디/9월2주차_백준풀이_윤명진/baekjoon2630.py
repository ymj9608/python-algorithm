def divide_paper(li, size):
    global blue_count
    global white_count

    b_count = 0
    w_count = 0

    for i in range(size):
        b_count += li[i].count(1)
        w_count += li[i].count(0)

    # 전부 파란색으로 칠해져 있다면 블루 카운트에 1 더하기
    if b_count == size ** 2:
        blue_count += 1


    # 전부 흰색으로 칠해져 있다면 흰색 카운트에 1 더하기
    elif w_count == size ** 2:
        white_count += 1

    # 그게 아니면 4개로 분할
    else:
        mid = size // 2

        # 제2사분면
        # row 범위: 0 ~ mid - 1, col 범위: 0 ~ mid - 1
        list_second = []
        for i in range(mid):
            list_second.append(li[i][:mid])

        divide_paper(list_second, mid)

        # 제1사분면
        # row 범위: 0 ~ mid - 1, col 범위: mid ~ size - 1
        list_first = []
        for i in range(mid):
            list_first.append(li[i][mid:])

        divide_paper(list_first, mid)

        # 제3사분면
        # row 범위: mid ~ size - 1, col 범위: 0 ~ mid - 1
        list_third = []
        for i in range(mid, size):
            list_third.append(li[i][:mid])

        divide_paper(list_third, mid)

        # 제4사분면
        # row 범위: mid ~ size - 1, col 범위: mid ~ size - 1
        list_fourth = []
        for i in range(mid, size):
            list_fourth.append(li[i][mid:])

        divide_paper(list_fourth, mid)


N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

blue_count = 0
white_count = 0

divide_paper(papers, N)

print(white_count)
print(blue_count)