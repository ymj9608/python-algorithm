

















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