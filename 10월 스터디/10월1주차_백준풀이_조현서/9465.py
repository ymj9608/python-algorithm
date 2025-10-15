# 스티커(아직 못풂) -> dp 문제
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
