from collections import deque

n,m= map(int, input().split())
grid_map=[]
distance = [[-1] * m for _ in range(n)]
queue = deque()


start_r ,start_c = -1, -1
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c] ==2: # 목표지점 찾기
            start_r, start_c = r, c
        elif row[c] ==0:
            distance[r][c] =0
       
    grid_map.append(row)



distance[start_r][start_c] = 0
queue.append((start_r,start_c))

dr=[-1,1,0,0]
dc=[0,0,-1,1]

while queue:
    r,c = queue.popleft()
    current_dist = distance[r][c]

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]

        if 0 <= nr < n and 0 <= nc <m:
            if distance[nr][nc] == -1:
                distance[nr][nc] =current_dist+1
                queue.append((nr,nc))

for r in range(n):
    for c in range(m):
        print(distance[r][c], end=' ')
        print()
