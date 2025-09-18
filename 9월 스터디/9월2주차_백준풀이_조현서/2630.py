# 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행과 열로 가면서 탐색
for i in range(N):
    for j in range(N):
        arr[i][j]

