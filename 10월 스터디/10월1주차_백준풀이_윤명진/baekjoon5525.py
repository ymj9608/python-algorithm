import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

is_I = False
is_O = False
count = 0
total_count = 0

for i in range(M):
    # 처음 I로 시작한 경우 I 정상 카운트
    if S[i] == 'I' and is_I is False and is_O is False:
        is_I = True
        count += 1

    # 처음 O로 시작한 경우
    elif S[i] == 'O' and is_I is False and is_O is False:
        is_O = True

    # IO
    elif S[i] == 'O' and is_I is True and is_O is False:
        is_I = False
        is_O = True
        count += 1

    # OI > IOI 체크 > 맞으면 total_count에 1 더하고, 연속된 IOI 카운트를 위해 count에서 2빼기
    elif S[i] == 'I' and is_I is False and is_O is True:
        is_I = True
        is_O = False
        count += 1

        if count == 2 * N + 1:
            total_count += 1
            count -= 2

    # OO > 전부 초기화
    elif S[i] == 'O' and is_I is False and is_O is True:
        count = 0

    # II > 전부 초기화, count는 1로 초기화
    elif S[i] == 'I' and is_I is True and is_O is False:
        count = 1


print(total_count)