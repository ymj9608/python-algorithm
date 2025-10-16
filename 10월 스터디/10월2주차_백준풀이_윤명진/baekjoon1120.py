import sys
input = sys.stdin.readline

A, B = input().rstrip().split()
min_diff = float('inf')

# 아이디어
# A = 'acg', B = 'aaacgbb'일 때,
# B를 A의 길이만큼 슬라이싱하여 확인하기 (aaa, aac, acg, cgb, gbb)
# 여기서 각 슬라이싱한 문자열을 A와 비교하여 차이의 최솟값 구하기
for i in range(len(B)-len(A) + 1):
    # B를 A의 길이만큼 추출
    new_B = B[i:i+len(A)]
    diff = 0
    for j in range(len(A)):
        if A[j] != new_B[j]:
            diff += 1

    min_diff = min(min_diff, diff)

print(min_diff)