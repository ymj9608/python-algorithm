# 회의실 배정(작업시간 문제랑 똑같음)
import sys
input = sys.stdin.readline

N = int(input())
# 튜플로 담음
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간으로 오름차순 
# 같을 경우 시작 시간으로 오름차순
meetings.sort(key = lambda x : (x[1], x[0]))

count = 0
last_end = 0

for start, end in meetings:
    # 시작시간이 전 마지막 시간보다 크면 카운트 + 1
    if start >= last_end:
        count += 1
        # 마지막 시간도 갱신해줌
        last_end = end

print(count)