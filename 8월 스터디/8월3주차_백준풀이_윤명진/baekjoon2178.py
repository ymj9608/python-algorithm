N, M = map(int, input().split())

my_list = [list(map(int, input())) for _ in range(N)]

def solve_with_stack(lst):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # (행, 열, 현재까지의 거리)를 기록할 스택
    stack = [(0, 0, 1)]

    # 각 칸까지의 최단 거리를 기록할 배열
    # 0은 아직 방문하지 않았음을 의미
    distance = [[0] * M for _ in range(N)]
    distance[0][0] = 1

    while stack:
        i, j, dist = stack.pop() # 스택의 가장 위 좌표와 거리를 꺼냄

        # 상, 하, 좌, 우 순서로 다음 경로 탐색
        for di, dj in moves:
            ni, nj = i + di, j + dj

            # 미로 범위 안에 있고, 이동 가능한 길인지 확인
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                # 2. 아직 방문하지 않았거나, 더 짧은 경로를 발견한 경우
                if distance[ni][nj] == 0 or distance[ni][nj] > dist + 1:
                    distance[ni][nj] = dist + 1 # 최단 거리 갱신
                    stack.append((ni, nj, dist + 1)) # 다음 탐색을 위해 스택에 추가

    # 도착 지점의 최단 거리를 반환
    return distance[N - 1][M - 1]

print(solve_with_stack(my_list))