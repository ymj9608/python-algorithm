N  = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# dfs로 구현
for i in range(1, N + 1):
    # i번째 그래프와 연결되어 있는 정점 탐색
    stack = [i]

    # 방문배열 생성
    visited = [0] * (N + 1)
    route = []
    while stack:
        now = stack.pop()

        # 현재의 그래프와 연결되어 있는 그래프 탐색
        for j in range(N):
            if graph[now - 1][j] == 1 and visited[j + 1] == 0:
                route.append(j + 1)
                stack.append(j + 1)
                visited[j + 1] = 1

    for node in route:
        graph[i - 1][node - 1] = 1

for row in graph:
    print(*row)