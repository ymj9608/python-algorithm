A, B = input().split()

X = len(A)
Y = len(B)

cnt = 0
if X == Y:
    for i in range(Y):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)

else:
    diff = Y - X
    new = ''
    diff_list = []
    for j in range(diff + 1):
        diff_cnt = 0
        new = B[:j] + A + B[X + j:]
        for p in range(Y):
            if new[p] != B[p]:
                diff_cnt += 1
        diff_list.append(diff_cnt)
    print(min(diff_list))