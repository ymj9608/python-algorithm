# 유기농 배추
'''
배추끼리 인접해있으면 그 배추들은 해충으로부터 보호받음
배추의 상하좌우 네 방향에 다른 배추가 있으면 인접한 것
필요한 최소의 배추 흰 지렁이 마리 수를 출력
'''
import sys
from collections import deque

input = sys.stdin.readline  

# 4방향(상하좌우) 탐색을 위한 이동 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  

    # 배추 위치를 기록할 밭
    field = [[0] * M for _ in range(N)]

    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worms = 0  # 필요한 지렁이 수

    # 모든 칸을 순회하며 BFS로 무리 개수 세기
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:      # 방문하지 않은 배추 발견
                worms += 1            # 새로운 무리 시작 -> 지렁이 +1
                field[y][x] = 0       # 방문 처리(바로 0으로 바꿔 재방문 방지)
                q = deque([(x, y)])

                while q:
                    cx, cy = q.popleft()
                    for i in range(4):
                        nx, ny = cx + dx[i], cy + dy[i]
                        if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                            field[ny][nx] = 0  # 방문 처리
                            q.append((nx, ny))

    print(worms)


