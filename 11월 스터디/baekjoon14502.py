from copy import deepcopy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]
first_visited = [[0] * M for _ in range(N)]
empty = []
virus = []
wall_count = 0
for i in range(N):
    for j in range(M):
        # 빈 공간의 좌표 체크
        if area[i][j] == 0:
            empty.append((i, j))

        # 벽 지역 체크 (방문처리하여 방문할 수 없게 수정)
        elif area[i][j] == 1:
            first_visited[i][j] = 1
            wall_count += 1

# 빈 공간에서 3개 뽑는 경우 담기
three_select = list(combinations(empty, 3))
min_count = N * M

for loc in range(len(three_select)):
    copy_area = deepcopy(area)
    visited = deepcopy(first_visited)

    # 각각의 3개를 뽑는 경우마다 벽 3개를 세운 다음 BFS
    (fi, fj), (si, sj), (ti, tj) = three_select[loc][0], three_select[loc][1], three_select[loc][2]

    copy_area[fi][fj] = copy_area[si][sj] = copy_area[ti][tj] = 1
    visited[fi][fj] = visited[si][sj] = visited[ti][tj] = 1
    count = 0

    for i in range(N):
        for j in range(M):
            # 바이러스 구역
            # 현재 구역이 바이러스가 있는 곳이고 방문하지 않았다면, BFS 탐색
            if copy_area[i][j] == 2 and visited[i][j] == 0:
                q = deque([(i, j)])
                visited[i][j] = 1
                count += 1
                while q:
                    ti, tj = q.popleft()

                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = ti + di, tj + dj
                        # 현재 구역이 바이러스이면서 인접 지역을 방문하지 않았다면, 바이러스가 인접구역으로 퍼짐
                        if 0 <= ni < N and 0 <= nj < M and copy_area[ti][tj] == 2 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            copy_area[ni][nj] = 2
                            q.append((ni, nj))
                            count += 1
    # 안전구역의 최대 영역은 바이러스 영역의 최솟값을 구하면 됨
    min_count = min(min_count, count)

# 안전구역 수의 최댓값 = 전체 크기(N * M) - 바이러스 영역수의 최솟값 - 벽의 개수
safety_area = N * M - min_count - wall_count - 3
print(safety_area)