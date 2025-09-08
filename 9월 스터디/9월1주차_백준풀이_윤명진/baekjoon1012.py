from collections import deque

T = int(input())

for case in range(T):
    M, N, K = map(int, input().split())

    my_list = [[0] * M for _ in range(N)]

    # a, b가 반대로 되어 있음
    for _ in range(K):
        a, b = map(int, input().split())
        my_list[b][a] = 1

    visited = [[0] * M for _ in range(N)]

    count = 0

    # bfs 탐색
    for i in range(N):
        for j in range(M):
            # 배추가 심어져 있고, 방문하지 않았다면 q 탐색 시작
            if my_list[i][j] == 1 and visited[i][j] == 0:
                q = deque([[i, j]])
                visited[i][j] = 1
                count += 1
                while q:
                    ti, tj = q.popleft()
                    
                    # 델타탐색으로 인접한 곳에 배추가 심어져 있고, 방문하지 않았다면, 방문처리 후 q에 추가
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = ti + di, tj + dj
                        if 0 <= ni < N and 0 <= nj < M and my_list[ni][nj] != 0 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append([ni, nj])

    print(count)