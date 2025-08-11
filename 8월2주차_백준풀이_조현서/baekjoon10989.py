# 수 정렬하기
N = int(input())

nums = []

for _ in range(N):
    num =int(input())
    nums.append(num)
    
    for i in range(N):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    
    for n in nums:
        print(n)












# 아래처럼 했더니 메모리 초과 결과가 나옴

# N = int(input())        # 수의 개수 N 설정

# nums = []               # 문자를 담을 리스트를 만듦

# for _ in range(N):      # N 만큼 반복하면서 문자를 하나씩 받음
#     num = int(input())
#     nums.append(num)    # 하나씩 받은 num을 리스트에 담음  

# nums.sort()             # 오름차순으로 정렬

# for n in nums:          # 한 줄씩 출력하기 위해서 nums 리스트에서 
#     print(n)            # 하나씩 뽑아 반복을 통해 출력


