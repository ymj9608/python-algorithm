T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort(reverse=True)
    B_list.sort(reverse=True)

    A_point = 0
    B_point = 0
    cnt = 0

    while A_point < A:
        if A_list[A_point] > B_list[B_point]:
            cnt += B
            A_point += 1
        else:
            if B_point < len(B_list) - 1:
                B_point += 1
                B -= 1
            else:
                A_point += 1

    print(cnt)