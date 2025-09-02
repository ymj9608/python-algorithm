# 제로
'''
문제를 처음에 잘못 이해해서 
0 개수만큼 최근 값들을 제거하는 게 아니라
0 바로 전의 값만 제거하는 줄 알고 풀었다가 틀림
'''
import sys
input = sys.stdin.readline

K = int(input())
nums = []

# K줄만큼 정수가 주어짐
for i in range(K):
    num = int(input())

    # 전에 나온 숫자가 있고
    # 현재 나온 숫자가 0일 경우
    # 가장 최근에 들어간 숫자를 제거
    if nums and num == 0:
        nums.pop()

    # 아니면 숫자를 그대로 넣음
    else:
        nums.append(num)

total = 0
for n in nums:
    total += n

print(total)
# print(sum(nums))