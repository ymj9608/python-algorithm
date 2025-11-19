import sys

input = sys.stdin.readline

N = int(input())

# 5kg 봉지를 최대한 많이 가져가는 것이 이득

# 5kg짜리 봉지와 3kg짜리 봉지의 수
fives = 0
threes = 0
while True:
    # 5로 나누어 떨어질 경우, fives와 threes를 더한 값을 출력 후 종료
    if N % 5 == 0:
        fives = N // 5
        print(fives + threes)
        break

    else:
        # 3kg짜리 봉지 한개씩 추가해보기 (남은 양은 N - 3)
        N -= 3
        threes += 1

        # N이 0보다 작아질 경우, 배달 불가능하므로 -1 출력
        if N < 0:
            print(-1)
            break