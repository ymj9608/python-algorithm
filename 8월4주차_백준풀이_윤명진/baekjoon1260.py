from collections import deque
N, M, V = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

# 양방향 연결 리스트 생성
adj_list = [[] for _ in range(N+1)]
for i, j in graph:
    adj_list[i].append(j)
    adj_list[j].append(i)

# 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문하기 위해 정렬 미리하기
for i in range(N+1):
    adj_list[i].sort()

# 방문한 지점인지 체크할 visited_DFS 생성
visited_DFS = [False] * (N + 1)
DFS_route = []

# dfs는 재귀함수로 구현
def dfs(v):
    visited_DFS[v] = True
    DFS_route.append(v)

    # 방문 안했다면, 재귀함수로 깊이 탐색
    for next_node in adj_list[v]:
        if not visited_DFS[next_node]:
            dfs(next_node)

# dfs 호출하여 수행 결과 출력
dfs(V)
print(" ".join(map(str, DFS_route)))

# bfs
visited_BFS = [0 for _ in range(N + 1)]
q_BFS = deque([V])
visited_BFS[V] = 1
BFS_route = []

while q_BFS:

    now = q_BFS.popleft()
    BFS_route.append(now)
    for next_node in adj_list[now]:
        if visited_BFS[next_node] == 0:
            q_BFS.append(next_node)
            visited_BFS[next_node] = 1


print(" ".join(map(str, BFS_route)))