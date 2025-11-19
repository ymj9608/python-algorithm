# 문자열 집합
'''
처음에 리스트로 했더니 시간 초과
-> set 함수 사용
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
include_list = {input().strip() for _ in range(N)}

count = 0
for _ in range(M):
    check = input().strip()
    if check in include_list:
        count += 1

print(count)