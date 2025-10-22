# 문자열
'''
앞뒤에 붙이는 건 아무 알파벳이나 가능하므로 
고려할 필요 X
A 문자열이 B 문자열 안에서 얼마나 겹치는지 확인하면 됨
'''
import sys
input = sys.stdin.readline

A, B = input().strip().split()

min_cnt = 1e9
count = 0
# 1. 문자열의 길이가 같은 경우 
# => 그냥 그대로 비교하면 됨
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
        min_cnt = count

# 2. 문자열의 길이가 A가 B보다 작은 경우
elif len(A) < len(B):
    # 길이 차이만큼 순회
    # A 길이만큼씩 잘라서 확인
    for i in range(len(B) - len(A) + 1):
        count = 0
        b = B[i:i+len(A)]
        for j in range(len(A)):
            if A[j] != b[j]:
                count += 1

        min_cnt = min(count, min_cnt)

print(min_cnt)