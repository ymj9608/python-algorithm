# 아직 백준에서는 안돌려본 코드 - 시간초과 날 수도 있음 ㅜㅜ!

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0 

# 바이러스 확산시켜봄
def virus():
    global result
    temp_mat = [row[:] for row in mat]
    queue = deque()
    
    # 초기 바이러스 위치
    for i in range(N):
        for j in range(M):
            if temp_mat[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바이러스 확산
            if 0 <= nx < N and 0 <= ny < M and temp_mat[nx][ny] == 0:
                temp_mat[nx][ny] = 2 
                queue.append((nx, ny))
                
    # 안전 영역 계산
    safe_cnt = sum(row.count(0) for row in temp_mat)
    result = max(result, safe_cnt)


# 벽 3개를 세워서 탐색
def wall(cnt):
    # 벽 3개를 모두 세웠다면 바이러스 확산시켜서 확인
    if cnt == 3:
        virus() 
        return
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                mat[i][j] = 1               
                wall(cnt + 1)
                mat[i][j] = 0

wall(0)
print(result)