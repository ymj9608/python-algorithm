import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
call = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
nums = []
for i in range(5):
    for item in call[i]:
        nums.append(item)
mat = [[0] * 5 for _ in range(5)]

def bingo():
    # 완성된 빙고 줄의 개수
    bingo_num = 0

    # 가로줄 빙고 조건 
    for i in range(5):
        if mat[i] == [1, 1, 1, 1, 1]:
            bingo_num += 1

    # 세로줄 빙고 조건
    for j in range(5):
        if mat[0][j] == 1 and mat[1][j] == 1 and mat[2][j] == 1 and mat[3][j] == 1 and mat[4][j] == 1:
            bingo_num += 1

    # 대각선 (\) 빙고 조건
    if mat[0][4] == 1 and mat[1][3] == 1 and mat[2][2] == 1 and mat[3][1] == 1 and mat[4][0] == 1:
        bingo_num += 1
    
    # 대각선 (/) 빙고 조건
    if mat[0][0] == 1 and mat[1][1] == 1 and mat[2][2] == 1 and mat[3][3] == 1 and mat[4][4] == 1:
        bingo_num += 1
    return bingo_num

for idx in range(25):
    item = nums[idx]
    flag = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == item:
                mat[i][j] = 1
                flag = True
                break
        if flag:
            break  
        # 숫자 찾으면 내부 j 루프, 외부 i 루프 break  

    if bingo() >= 3:
        # 현재까지 부른 숫자의 개수 출력
        print(idx+1)
        break