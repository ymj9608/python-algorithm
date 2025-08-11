# 셀렉션 알고리즘
# k번째 원소만 찾는 것



# 시간 초과
# N, K 입력
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# 선택 정렬을 K번째 원소까지 수행
# for i in range(K):  # 0 ~ K-1까지만
#     min_idx = i
#     for j in range(i + 1, N):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
# 최소값과 현재 위치를 교환
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# K번째 원소 출력 (인덱스는 K-1)
# print(arr[K - 1])


















# 시간 초과(버블 정렬 형태로 풂)
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