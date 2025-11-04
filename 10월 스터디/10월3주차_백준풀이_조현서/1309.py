# 동물원
'''
가로로 세로로도 붙을 수 없음
인접하면 배치 불가
사자를 배치하는 경우의 수 -> 한 마리도 배치하지 않는 경우도 존재
'''
import sys
input = sys.stdin.readline

N = int(input())

# 왼쪽에 먼저 두는 경우
left = 1
# 오른쪽에 먼저 두는 경우
right = 1
# 아예 안 두는 경우
blank = 1

# 첫째 줄에 사자를 배치함
for _ in range(1, N):
    # 다음 왼쪽 = 전의 오른쪽이나 공백
    next_left = right + blank
    # 다음 오른쪽 = 전의 왼쪽이나 공백
    next_right = left + blank
    # 다음 공백 = 전에 모든 경우 가능
    next_blank = left + right + blank

    left = next_left
    right = next_right
    blank = next_blank

print((left + right + blank) % 9901)    