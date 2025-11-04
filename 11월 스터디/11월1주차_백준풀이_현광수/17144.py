import math, copy

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
total_dust = 0

up_row = -1
down_row = -1
for i in range(R):
    if room[i][0] == -1:
        up_row = i
        down_row = i + 1
        break

for _ in range(T):
    # 동시에 퍼지는 과정을 구현하기 위한 임시 방 구현
    temp_room = [[0 for _ in range(C)] for _ in range(R)]
    # 먼지 퍼지는 과정
    temp_room[up_row][0] = -1
    temp_room[down_row][0] = -1
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                L = math.trunc(room[i][j] / 5)
                cnt = 0
                for d in range(4):
                    di = i + dirs[d][0]
                    dj = j + dirs[d][1]

                    if 0 <= di < R and 0 <= dj < C and room[di][dj] != -1:
                        temp_room[di][dj] += L
                        cnt += 1
                temp_room[i][j] += (room[i][j] - (L * cnt))

    room = copy.deepcopy(temp_room)

    # 공기청정기 작동 과정
    # 위쪽 공기청정기
    for x in range(up_row - 1, 0, -1):
        room[x][0] = room[x - 1][0]

    for y in range(C - 1):
        room[0][y] = room[0][y + 1]

    for x in range(up_row):
        room[x][C - 1] = room[x + 1][C - 1]

    for y in range(C - 1, 1, -1):
        room[up_row][y] = room[up_row][y - 1]

    room[up_row][1] = 0

    # 아래쪽 공기 청정기
    for x in range(down_row + 1, R - 1):
        room[x][0] = room[x + 1][0]

    for y in range(C - 1):
        room[R - 1][y] = room[R - 1][y + 1]

    for x in range(R - 1, down_row, -1):
        room[x][C - 1] = room[x - 1][C - 1]

    for y in range(C - 1, 1, -1):
        room[down_row][y] = room[down_row][y - 1]

    room[down_row][1] = 0

for g in range(R):
    for h in range(C):
        if room[g][h] > 0:
            total_dust += room[g][h]

print(total_dust)