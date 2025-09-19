# 나무 자르기(이진 탐색 -> 시간초과)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

low = 0
high = max(heights)

while low <= high:
    mid = (low + high) // 2
    tree = 0
    # 나무 길이가 절단기보다 크면 
    # 그 차이가 나무의 개수에 더해짐 
    for height in heights:
        if height > mid:
            tree += height - mid
    
    # 목표 나무 개수보다 크면 나무를 줄여야 함
    # -> 절단기 높이를 올림
    # 같으면 중간값(절단기 높이)이 정답
    if tree >= M:
        low = mid + 1
    # 작아지면 나무를 늘려야 함
    # -> 절단기 높이를 내림
    else:
        high = mid - 1

print(high)