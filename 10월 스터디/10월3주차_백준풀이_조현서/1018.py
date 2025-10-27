# 체스판 다시 칠하기
'''
어려움,,
'''
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().strip()) for _ in range(N))

# 왼쪽 위부터 시작
# 8 * 8 배열 탐색 
for start_row in range(N - 7):
    for start_col in range(M - 7):
        change_b = 0
        change_w = 0

        for i in range(8):
            for j in range(8):
                next_row = start_row + i
                next_col = start_col + j

                if j % 2 == 1:
                    if arr[i][j] != 'W':
                        change_b += 1
            