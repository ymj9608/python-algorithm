from collections import deque
import sys

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())

    # 종료 조건
    if w == 0 and h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    total_cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([(i, j)])
                total_cnt += 1
                while q:
                    ti, tj = q.popleft()

                    # 가로, 세로 대각선 8방향 델타 탐색
                    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                        ni, nj = ti + di, tj + dj
                        # 범위 벗어나면 다음 방향 탐색
                        if not (0 <= ni < h and 0 <= nj < w):
                            continue

                        # 인접 지형이 섬이고, 방문하지 않았다면 q에 추가, 방문처리
                        if maps[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append((ni, nj))

    print(total_cnt)