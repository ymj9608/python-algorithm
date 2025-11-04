# 창고 다각형
import sys
input = sys.stdin.readline
N = int(input())

# N이 1000까지이므로
min_side = 1000
max_side = 0
height = [0] * 1001

for _ in range(N):
    L, H = map(int, input().split())
    # 높이 부여
    height[L] = H
    # 시작점과 끝점 갱신
    min_side = min(min_side, L)
    max_side = max(max_side, L)

left_max = [0] * 1001
right_max = [0] * 1001

# 왼쪽부터 탐색
h = 0
for i in range(min_side, max_side + 1):
    h = max(h, height[i])
    left_max[i] = h

# 오른쪽 탐색(역순)
h = 0
for i in range(max_side, min_side - 1, -1):
    h = max(h, height[i])
    right_max[i] = h
# print(left_max)
# print(right_max)

# 각 기둥 위치의 최종 높이는 좌우에서 본 최댓값 중 작은 값
area = 0
for i in range(min_side, max_side + 1):
    final_h = min(left_max[i], right_max[i])
    area += final_h

print(area)