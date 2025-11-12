# 별 찍기 - 19
'''
n = 1 => 별 하나
그 뒤로는 별을 둘러싸는 사각형 n-1개씩 늘어남 
생기는 사각형은 전 사각형의 가로세로 길이 +4칸씩 증가(재귀 함수)
=> 상하좌우로 2칸씩 증가
'''
import sys
input = sys.stdin.readline

def star(x, y, n):
    # n=1이면 별 하나
    if n == 1:
        board[x][y] = '*'
        return
    
    length = 4 * n - 3

    # 윗줄
    for i in range(length):
        board[x][y + i] = '*'
    # 아랫줄
    for i in range(length):
        board[x + length - 1][y + i] = '*'
    # 왼쪽줄
    for i in range(length):
        board[x + i][y] = '*'
    # 오른쪽줄
    for i in range(length):
        board[x + i][y + length - 1] = '*'

    # 그 다음 안쪽 사각형 재귀함수
    star(x + 2, y + 2, n - 1)

n = int(input())

# 가로세로 크기(4칸씩 증가)
size = 4 * n - 3  
board = [[' '] * size for _ in range(size)]
star(0, 0, n)

# 한 줄씩 출력
for row in board:
    print(''.join(row))