from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

rgbs = [list(input()) for _ in range(N)]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

total_non_count = 0
total_count = 0

visited = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 방문 안했으면
        if visited[i][j] == 0:
            # 지금의 색을 current_color에 저장
            current_color = rgbs[i][j]
            q = deque([(i, j)])
            visited[i][j] = 1
            total_non_count += 1

            while q:
                ti, tj = q.popleft()

                for di, dj in moves:
                    ni, nj = ti + di, tj + dj
                    # 인접한 지역이 방문하지 않은 곳이고, 현재의 색과 같으면 방문처리, q에 추가
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and rgbs[ni][nj] == current_color:
                        visited[ni][nj] = 1
                        q.append((ni, nj))


        if visited_2[i][j] == 0:
            # 지금의 색을 current_color에 저장
            current_color = rgbs[i][j]
            q = deque([(i, j)])
            visited_2[i][j] = 1
            total_count += 1

            while q:
                ti, tj = q.popleft()

                for di, dj in moves:
                    ni, nj = ti + di, tj + dj
                    # 적록색약인 경우 (빨강과 초록을 구분하지 못함)
                    if 0 <= ni < N and 0 <= nj < N and visited_2[ni][nj] == 0 and current_color in ['R', 'G'] and rgbs[ni][nj] in ['R', 'G']:
                        visited_2[ni][nj] = 1
                        q.append((ni, nj))

                    # 인접한 지역이 방문하지 않은 곳이고, 현재의 색과 인접한 지역의 색이 모두 파란색이면 방문처리, q에 추가
                    elif 0 <= ni < N and 0 <= nj < N and visited_2[ni][nj] == 0 and current_color == 'B' and rgbs[ni][nj] == 'B':
                        visited_2[ni][nj] = 1
                        q.append((ni, nj))

print(total_non_count, total_count)