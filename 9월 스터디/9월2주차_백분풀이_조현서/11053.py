# 가장 긴 증가하는 부분 수열
'''
수열 A가 주어지면 증가하는 부분에 해당하는
수열의 길이를 구함
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N):
    # 현재 원소가 이전 원소보다 커지면
    # 카운트 + 1
    if nums[i] > nums[i - 1]:
        count += 1
    # 아니면 넘김
    else:
        continue

print(f'{count + 1}')