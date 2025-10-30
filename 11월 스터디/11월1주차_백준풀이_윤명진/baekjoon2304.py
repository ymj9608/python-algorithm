import sys
input = sys.stdin.readline

N = int(input())
rectangles = [list(map(int, input().split())) for _ in range(N)]

rectangles.sort()

# 가장 높은 직사각형의 높이 찾기
max_height = 0
for i in range(N):
    max_height = max(max_height, rectangles[i][1])

# 가장 높은 직사각형의 인덱스 찾기
max_idx_list = []
for i in range(N):
    if rectangles[i][1] == max_height:
        max_idx_list.append(i)

# 가장 높은 직사각형의 인덱스가 여러개이면 첫 인덱스와 마지막 인덱스 사이는 전부 최대 높이로 지정
first_max_idx = max_idx_list[0]
last_max_idx = max_idx_list[-1]

total_area = 0

# 가장 높은 직사각형의 왼쪽 부분 영역 더하는 과정
max_left = rectangles[0]
for i in range(1, first_max_idx + 1):  # 첫 번째 최대 높이 기둥 *포함*
    current_rectangle = rectangles[i]

    # 현재 직사각형이 왼쪽 최대 높이보다 높거나 같으면
    if current_rectangle[1] >= max_left[1]:
        # 영역 더해주기
        total_area += max_left[1] * (current_rectangle[0] - max_left[0])
        # 최대 높이 갱신
        max_left = current_rectangle

# 오른쪽 부분 영역 더하는 과정
max_right = rectangles[N - 1]
for i in range(N - 2, last_max_idx - 1, -1):
    current_rectangle = rectangles[i]

    if current_rectangle[1] >= max_right[1]:
        total_area += max_right[1] * (max_right[0] - current_rectangle[0])
        max_right = current_rectangle

# 최대 높이 부분 영역 더하기
total_area += max_height * (rectangles[last_max_idx][0] - rectangles[first_max_idx][0] + 1)

print(total_area)