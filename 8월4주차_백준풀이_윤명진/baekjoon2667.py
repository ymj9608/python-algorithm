from collections import deque

N = int(input())

my_list = [list(map(int, input())) for _ in range(N)]

# 방문체크
visited = [[0] * N for _ in range(N)]

# alpha: 단지
alpha = 0
count_list = []
for i in range(N):
    for j in range(N):
        # 집이 있는 곳이며, 방문하지 않았을 경우
        if my_list[i][j] == 1 and visited[i][j] == 0:
            q = deque([[i, j]])
            alpha += 1
            # visited에 단지번호로 저장
            visited[i][j] = alpha
            # 총 몇개의 집이 있는지 체크할 count 변수 생성
            count = 1
            # bfs
            while q:
                ti, tj = q.popleft()

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = ti + di, tj + dj
                    # 델타탐색으로 방문하지 않았고, 벽이 아니라면 탐색
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and my_list[ni][nj] != 0:
                        # 해당 지점도 단지번호를 붙이고, q에 추가
                        visited[ni][nj] = alpha
                        q.append((ni, nj))
                        count += 1
            count_list.append(count)

count_list.sort()
print(alpha)

for i in range(alpha):
    print(count_list[i])
