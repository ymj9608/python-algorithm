# 수 찾기(시간 초과났었음)
# 정렬은 내장 sort() 사용
# 최대한 배운 내용을 하기 위해 이진탐색을 사용해봄
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()  # 오름차순 정렬(이진 탐색을 하기위해서)

def binary_search(arr, target):       # 배열과 목표값을 넣으면 이진탐색
    left = 0                       # 왼쪽을 0, 오른쪽을 배열의 길이의 인덱스 끝 값 배정
    right = len(arr) - 1

    while left <= right:           # 왼쪽 끝이 오른쪽 끝보다 작을 경우 계속 반복
        mid = (left + right) // 2  # 중심값 설정
        num = arr[mid]             # 인덱스 중심값의 값을 num에 설정
        if num == target:
            return 1
        if num < target:           # 목표값이 인덱스 중심값보다 오른쪽에 있을 경우
                                   # 인덱스 첫 지점을 중앙값 오른쪽으로 이동
            left = mid + 1
        else:                      # 반대의 경우
                                   # 인덱스 마지막 값을 중앙값 왼쪽으로 이동
            right = mid - 1
    return 0

for n in B:                        # B에서 하나씩 꺼내어 함수를 이용해 목표값을 A 배열에서 찾음
    print(binary_search(A, n))


# 시간 초과났었던 코드
# for char1 in b:
#     if char1 in a:
#         print('1')

#     else:
#         print('0')