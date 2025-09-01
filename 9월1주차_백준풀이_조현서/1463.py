# 1로 만들기
import sys
input = sys.stdin.readline

N = int(input())

# 연산할 때마다 셀 카운트 생성
count = 0
# 최솟값 기본값 설정
min_cnt = 10e9

# N이 1이 되는 순간 종료
while N != 1:
    if N == 1:
        break

    # 3으로 나눠지면 3으로 나눔
    if N % 3 == 0:
        N = N // 3
        
    # 2로 나눠지면 2로 나눔
    elif N % 2 == 0:
        N = N // 2

    # 모두 아니면 그냥 -1
    else:
        N = N - 1

    # 한 과정이 끝나면 카운트 + 1    
    count += 1

if count < min_cnt:
    min_cnt = count

print(min_cnt)
 