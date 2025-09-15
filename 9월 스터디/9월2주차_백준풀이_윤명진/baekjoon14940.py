from collections import deque
n, m = map(int, input().split())

my_list = [list(map(int, input().split())) for _ in range(n)]

# 최소 거리를 저장할 방문 배열 생성
visited = [[-1] * m for _ in range(n)]

# 0이면 못가는 경로이므로 visited를 0으로 세팅
for i in range(n):
    for j in range(m):
        if my_list[i][j] == 0:
            visited[i][j] = 0

        # 시작점 찾기
        elif my_list[i][j] == 2:
            si, sj = i, j

# bfs로 구현, q에는 [행, 열, 거리]로 저장
q = deque([[si, sj, 0]])
visited[si][sj] = 0

while q:
    ti, tj, dis = q.popleft()

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = ti + di, tj + dj

        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
            visited[ni][nj] = dis + 1
            q.append([ni, nj, visited[ni][nj]])

for row in visited:
    print(*row)