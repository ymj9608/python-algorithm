# 블랙잭
N, M = map(int,input().split())         # 카드의 개수 N, 딜러가 부르는 숫자 M
nums = list(map(int, input().split()))  # 카드에 쓰여있는 수 리스트 작성

max_value = 0                           # M을 넘지 않는 최댓값 설정

# 그럼 이제 N 장 중 3장을 골라 3장의 합이 M과 같거나 작게 만드는 로직 필요
for i in range(N):
    for j in range(i+1, N):             # N 까지 반복하면서 i, j, k는 인덱스값이므로
        for k in range(j+1, N):         # nums[] 형태로 값을 변환
            total = nums[i] + nums[j] + nums[k]

            if total <= M:
                max_value = max(max_value, total)

print(max_value)



# 중복된 숫자를 고를 수도 있기 때문에 이 로직은 맞지 않음
# for i in nums:
#     for j in nums:
#         for k in nums:
#             if i + j + k <= M:
