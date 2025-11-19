T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()

    eat = 0
    for a in A:
        # 한 번이라도 먹었는지 체크
        check = False
        for b in B:
            if a > b:
                eat += 1
                check = True
            # 못 먹는 순간 뒤에 더 먹을 수 없으므로 종료
            else:
                break
        # 한 번도 못 먹었으면 뒷번호도 못 먹으니까 종료
        if check == False:
            break

    print(eat)