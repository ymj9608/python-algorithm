import sys
input = sys.stdin.readline

N = int(input())

# 왼쪽 배치한 경우, 오른쪽 배치한 경우, 배치 안한 경우
left = 1
right = 1
empty = 1

for i in range(1, N):
    # i번째 왼쪽 배치한 경우의 수 = i-1번째 오른쪽 배치한 경우의 수 + i-1번째 배치 안한 경우의 수
    new_left = right + empty

    # i번째 오른쪽 배치한 경우의 수 = i-1번째 왼쪽 배치한 경우의 수 + i-1번째 배치 안한 경우의 수
    new_right = left + empty

    # i번째 배치 안한 경우의 수 = i-1번째 왼쪽 배치한 경우의 수 + i-1번째 오른쪽 배치한 경우의 수 + i-1번째 배치 안한 경우의 수
    new_empty = left + right + empty

    # 왼쪽, 오른쪽, 배치안한 경우 갱신
    left, right, empty = new_left % 9901, new_right % 9901, new_empty % 9901

print((left + right + empty) % 9901)