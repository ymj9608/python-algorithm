# 수 찾기(시간 초과)
# 정렬은 내장 sort() 사용, 탐색은 직접 구현 (학습용)
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()  # 오름차순 정렬

def bin_search(arr, target):
    left = 0 
    right = len(arr) - 1

    while left <= right:  # 왼쪽 끝이 오른쪽 끝보다 작을 경우 계속 반복
        mid = (left + right) // 2 # 중심값
        num = arr[mid]
        if num == target:
            return 1
        if num < target:  # 목표값이 오른쪽에 있을 경우 
                          # 왼쪽부분을 중앙값 오른쪽에 위치시킴
            left = mid + 1
        else:             # 반대의 경우 오른쪽 부분을 
                          # 중앙값 왼쪽에 위치시킴
            right = mid - 1
    return 0

for n in B:
    print(bin_search(A, n))


# 시간 초과
# for char1 in b:
#     if char1 in a:
#         print('1')

#     else:
#         print('0')