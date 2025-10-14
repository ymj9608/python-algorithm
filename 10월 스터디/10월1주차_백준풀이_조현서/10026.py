# 적록색약
'''
적록색약은 R=G로 취급
상하좌우
'''
from collections import deque
import sys
input = sys.stdin.readline

# BFS 탐색
def bfs(x, y, arr, visited):
    n = len(arr)
    q = deque([(x, y)])
    visited[x][y] = True
    color = arr[x][y]

    # 상하좌우 델타 
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        cx, cy = q.popleft()

        # 상하좌우 이동
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않고 다음 구역이 같은 색이면 계속 탐색
                if not visited[nx][ny] and arr[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 구역 세기          
def count_areas(arr):
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, arr, visited)
                count += 1
    return count

N = int(input())
arr = [list(input()) for _ in range(N)]

# 적록색약용 arr 만들기
rg_arr = []

for row in arr:
    new_row = [] 

    for color in row:
        # G는 R로 바꿈
        if color == 'G':       
            new_row.append('R')
        
        # R과 B는 그대로 추가
        else:
            new_row.append(color)  

    # 완성된 줄을 적록색약 배열에 추가
    rg_arr.append(new_row)

# 일반인 시선
normal = count_areas(arr)
# 적록색약 시선
rg = count_areas(rg_arr)

print(normal, rg)