import sys
input = sys.stdin.readline

N = int(input())

my_list = [list(map(int, input().split())) for _ in range(N)]

# 종료 시간 순으로 정렬, 종료 시간이 같으면 시작 시간 순으로 정렬
my_list.sort(key=lambda x: (x[1], x[0]))

# 마지막 종료 시간을 저장할 변수 생성
last_end = -1
done = 0

# 시작 시간이 마지막 종료 시간보다 크면 done에 1 더하고, 마지막 종료 시간을 현재 종료 시간으로 갱신
for start, end in my_list:
    if start < last_end:
        continue

    done += 1
    last_end = end

print(done)