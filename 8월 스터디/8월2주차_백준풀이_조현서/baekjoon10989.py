# 수 정렬하기 -> 오름차순
import sys
input = sys.stdin.readline  # 빠른 입력을 위해 import 사용

N = int(input())            # 밑의 과정은 시간 초과된 코드과 똑같음
counts = [0] * 10001

for _ in range(N):
    num = int(input())
    counts[num] += 1

for i in range(1, 10001):
    count = counts[i]
    if count == 0:
        continue
    for _ in range(count):
        print(i)

# 카운팅 정렬 적용(시간 초과) -----------------------------------------------------------------
# N = int(input())
#
# # 각 수의 등장 횟수를 저장할 '카운트 배열' 만들기
# # 길이가 10001이어야 인덱스 10000 접근 가능
# counts = [0] * 10001
#
# for _ in range(N):          # N번 반복하면서 해당 num의 카운트를 +1
#     num = int(input())      # 한 줄씩 N개의 정수가 주어지므로
#     counts[num] += 1        # num가 나올때마다 카운트 증가
#
# for i in range(1, 10001):   # 1~10000까지의 인덱스를 돌면서(1부터 시작인 이유는 num가 자연수이므로)
#     count = counts[i]       # 숫자 i가 몇개 나왔는지 확인
#     if count == 0:
#         continue            # 한 번도 안 나왔으면 건너뜀
#     for _ in range(count):
#         print(i)            # 카운트가 있다면 카운트만큼 i를 반복 출력

# 버블 정렬을 사용했더니 메모리 초과가 뜸--------------------------------------------------------
# N = int(input())
# nums = []

# for _ in range(N):
#     num = int(input())
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


