T = int(input())

for case in range(1, T+1):
    N = int(input())
    my_str1 = input()
    my_str2 = input()

    wb_count = 0
    bw_count = 0
    # 초기 상태의 i번째 인덱스가 W, 목표 상태의 i번쨰 인덱스가 B이면 wb_count에 1 추가
    # 초기 상태의 i번째 인덱스가 B, 목표 상태의 i번쨰 인덱스가 W이면 bw_count에 1 추가
    for i in range(N):
        if my_str1[i] == 'W' and my_str2[i] == 'B':
            wb_count += 1
        elif my_str1[i] == 'B' and my_str2[i] == 'W':
            bw_count += 1

    # wb_count가 bw_count보다 크거나 같으면 wb_count 출력
    if wb_count >= bw_count:
        print(wb_count)
    # bw_count가 wb_count보다 크면 bw_count 출력
    elif bw_count > wb_count:
        print(bw_count)
