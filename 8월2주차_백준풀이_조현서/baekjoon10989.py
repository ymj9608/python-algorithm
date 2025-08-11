# 수 정렬하기(카운팅 정렬 적용)
N = int(input())

# 각 수의 등장 횟수를 저장할 '카운트 배열' 만들기
#    인덱스가 "그 수 자체"가 되도록 0..10000까지 준비
#    문제 조건의 최대값이 10000이므로 길이는 10001이어야 index 10000 접근 가능
count = [0] * 10001 

# 3) N번 입력을 읽으면서 해당 숫자의 등장 횟수를 +1
for _ in range(N):
    x = int(input())   # 한 줄을 읽고 정수로 변환
    count[x] += 1      # x가 등장했으므로 카운트 증가


for i in range(1, 10001):
    c = count[i]       # 숫자 i의 등장 개수
    if c == 0:
        continue       # 한 번도 안 나왔으면 건너뜀
    for _ in range(c):
        print(i)       # i를 c번 출력



# 원래 하던대로 했더니 메모리 초과
# N = int(input())

# nums = []

# for _ in range(N):
#     num =int(input())
#     nums.append(num)
    
#     for i in range(N):
#         for j in range(i+1, N):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
    
    
#     for n in nums:
#         print(n)












# 아래처럼 했더니 메모리 초과 결과가 나옴

# N = int(input())        # 수의 개수 N 설정

# nums = []               # 문자를 담을 리스트를 만듦

# for _ in range(N):      # N 만큼 반복하면서 문자를 하나씩 받음
#     num = int(input())
#     nums.append(num)    # 하나씩 받은 num을 리스트에 담음  

# nums.sort()             # 오름차순으로 정렬

# for n in nums:          # 한 줄씩 출력하기 위해서 nums 리스트에서 
#     print(n)            # 하나씩 뽑아 반복을 통해 출력


