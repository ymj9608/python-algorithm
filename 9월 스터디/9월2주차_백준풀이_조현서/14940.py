# 쉬운 최단거리
'''
가로와 세로로만 이동 가능
'''
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1] * m for _ in range(n)]
start_x, start_y = 0, 0

# 배열에서 2의 위치를 찾고
# 그 좌표가 시작점
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_x, start_y = i, j

q = deque()
q.append((start_x, start_y))
dist[start_x][start_y] = 0

while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위 안
        if 0 <= nx < n and 0 <= ny < m:
            # 갈 수 있는 땅이고 방문하지 않은 곳이면 이동
            if arr[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 행마다 숫자 담는 과정
for i in range(n):
    row = []
    for j in range(m):
        # 목표지점 위치에는 0
        if arr[i][j] == 2:
            row.append(0)
        # 갈 수 없는 땅도 0
        elif arr[i][j] == 0:
            row.append(0)
        # 나머지는 지금까지 계산된 거리를 그대로 넣음
        else:
            row.append(dist[i][j])

    print(*row)