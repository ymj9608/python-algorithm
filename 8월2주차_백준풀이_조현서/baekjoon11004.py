# 셀렉션 알고리즘
# k번째 원소만 찾는 것
import sys                      # import 함수 출력
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

def quickselect(left, right, k_index):
    # left == right: 구간에 숫자가 하나뿐이면 바로 반환
    if left == right:
        return numbers[left]

    # 피벗: 구간의 중앙값 (임의 선택)
    mid = numbers[(left + right) // 2]

    # i: 왼쪽 포인터, j: 오른쪽 포인터
    i, j = left, right

    while i <= j:
        # 왼쪽에서 mid보다 큰 값 나올 때까지 이동
        while numbers[i] < mid:
            i += 1
        # 오른쪽에서 mid보다 작은 값 나올 때까지 이동
        while numbers[j] > mid:
            j -= 1
        # 양쪽 포인터가 교차 전이면 교환
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1

    # 이제 [left, j] 구간에는 mid 이하 값, [i, right] 구간에는 mid 이상 값이 있음

    # K번째 수가 왼쪽 그룹에 있으면 왼쪽 재탐색
    if k_index <= j:
        return quickselect(left, j, k_index)
    # K번째 수가 오른쪽 그룹에 있으면 오른쪽 재탐색
    elif k_index >= i:
        return quickselect(i, right, k_index)
    # 그 외에는 mid가 정답
    else:
        return numbers[k_index]

# K번째 수 출력 (인덱스는 0부터 시작하므로 K-1)
print(quickselect(0, N - 1, K - 1))

# 시간 초과 1 --------------------------------------------------------------------------------
# N, K 입력
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# 선택 정렬을 K번째 원소까지 수행
# for i in range(K):  # 0 ~ K-1까지만
#     min_idx = i
#     for j in range(i + 1, N):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]   # 최소값과 현재 위치를 교환
# K번째 원소 출력 (인덱스는 K-1)
# print(arr[K - 1])

# 시간 초과2(버블 정렬 형태로 풂) ---------------------------------------------------------------
# N, K = map(int, input().split())
# a = list(map(int, input().split()))

# for i in range(N):
#     for j in range(i+1, N):     
#         if a[i] > a[j]:                       # 뒤의 숫자가 더 클 경우
#             a[i], a[j] = a[j], a[i]           # 위치를 뒤바꿔줌(앞으로 오게끔)

# count = 0 
# for num in a:
#     count += 1
#     if count == K:
#         print(num)