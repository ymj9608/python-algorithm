import sys
input = sys.stdin.readline

N = int(input())
total_tips = 0
num_list = [int(input()) for _ in range(N)]

# 팁을 많이 주는 순으로 우선 입장하는 것이 최대팁 받을 수 있음
num_list.sort(reverse=True)

for i in range(N):
    # 최종 팁 = 예상 팁 - (받은 등수 - 1)
    tips = num_list[i] - i
    # 0보다 크거나 같으면 total_tips에 더하기
    if tips >= 0:
        total_tips += tips

print(total_tips)