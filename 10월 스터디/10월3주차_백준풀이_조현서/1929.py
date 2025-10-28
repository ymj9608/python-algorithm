# 소수 구하기
'''
소수는 말 그대로 1과 자기 자신만이 약수
자기 자신만 빼고 자신의 배수는 소수가 아님
'''
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# 0과 1은 소수 x 
nums = [False] + [False] + [True] * (N - 1)

# 2부터 N까지(0과 1은 False이므로)
for i in range(2, N + 1):
    if nums[i] == True:
        # 자기 자신은 빼야 하므로 다음 배수부터 빼주기
        # 다음 배수부터 i 배수에 해당하는 숫자 False
        for j in range(i + i, N + 1, i):
            nums[j] = False
# print(nums)

# 정리된 배열에서 소수를 하나씩 꺼냄
for i in range(M, N + 1):
    if nums[i] == True:
        print(i)