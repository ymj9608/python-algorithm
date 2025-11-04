# 빙고
'''
가로, 세로, 대각선을 고려해야 함
'''
board = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]
num_list = []

# 번호를 한 줄로 만듦
for row in nums:
    num_list.extend(row)

# 빙고판 숫자 위치 딕셔너리에 저장
pos = {}
for i in range(5):
    for j in range(5):
        pos[board[i][j]] = (i, j)
# print(pos)

# 행과 열마다 체크
row = [0] * 5
col = [0] * 5
# [우하향, 우상향]
diag = [0, 0]

count = 0

# 번호를 순서대로 부름
for num in num_list:
    # 번호 부를 때마다 카운트 + 1
    count += 1
    # 좌표를 꺼내서
    (r, c) = pos[num]
    row[r] += 1
    col[c] += 1

    # 행과 열이 같으면 우하향
    if r == c:
        diag[0] += 1
    # 행과 열의 합이 4이면 우상향
    if r + c == 4:
        diag[1] += 1

    # 빙고 개수
    bingo = row.count(5) + col.count(5) + diag.count(5)

    if bingo >= 3:
        print(count)
        break