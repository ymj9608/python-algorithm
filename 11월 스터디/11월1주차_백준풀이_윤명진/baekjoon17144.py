from copy import deepcopy
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
fine_dust = [list(map(int, input().split())) for _ in range(R)]

is_find_first = False
for i in range(R):
    for j in range(C):
        if not is_find_first and fine_dust[i][j] == -1:
            first_air_purifier = (i, j)
            is_find_first = True

        elif is_find_first and fine_dust[i][j] == -1:
            second_air_purifier = (i, j)

seconds = 0
while seconds < T:
    # 원래의 먼지의 양을 저장하기 위해 deepcopy 사용
    new_dust = deepcopy(fine_dust)
    seconds += 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            plus_dust = int(fine_dust[i][j] / 5)
            # 인접지역 체크
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                # 인접 지역에 공기청정기가 있으면 다음 탐색
                if 0 <= ni < R and 0 <= nj < C and fine_dust[ni][nj] == -1:
                    continue
                # 인접 지역이 유효한 지역이면 확산
                if 0 <= ni < R and 0 <= nj < C:
                    new_dust[ni][nj] += plus_dust
                    new_dust[i][j] -= plus_dust

    # 미세먼지 확산 후 다시 fine_dust 갱신
    fine_dust = deepcopy(new_dust)

    tr, tc = first_air_purifier

    # 첫번째 공기청정기 작동
    while True:
        new_dust = deepcopy(fine_dust)
        # 오른쪽
        new_dust[tr] = [-1, 0] + fine_dust[tr][1:C - 1]

        # 위
        for i in range(tr):
            new_dust[i][-1] = fine_dust[i + 1][-1]

        # 왼쪽
        new_dust[0] = fine_dust[0][1:C] + [new_dust[0][-1]]

        # 아래
        for i in range(1, tr):
            new_dust[i][0] = fine_dust[i - 1][0]

        fine_dust = deepcopy(new_dust)
        break

    tr, tc = second_air_purifier

    # 두번째 공기청정기 작동
    while True:
        new_dust = deepcopy(fine_dust)
        # 오른쪽
        new_dust[tr] = [-1, 0] + fine_dust[tr][1:C - 1]

        # 아래
        for i in range(tr, R - 1):
            new_dust[i + 1][-1] = fine_dust[i][-1]

        # 왼쪽
        new_dust[R - 1] = fine_dust[R - 1][1:C] + [new_dust[R - 1][-1]]

        # 위
        for i in range(tr + 1, R - 1):
            new_dust[i][0] = fine_dust[i + 1][0]

        fine_dust = deepcopy(new_dust)
        break

total_fine_dust = 0
# T초가 지났다면 미세먼지 카운트
for i in range(R):
    for j in range(C):
        # 공기청정기가 아닌 지역만 카운트
        if fine_dust[i][j] != -1:
            total_fine_dust += fine_dust[i][j]

print(total_fine_dust)