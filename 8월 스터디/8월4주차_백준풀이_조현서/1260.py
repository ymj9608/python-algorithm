# DFS와 BFS
'''
DFS 방식은 깊이 탐색으로써 한 곳으로 계속해서 깊이 탐색하는 방식
BFS 방식은 자기 자신과 인접한 부분을 모두 탐색하는 방식
이 2개의 방식의 차이점을 확실히 알아야 풀 수 있을 듯
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 큐 리스트를 정해주지 않았더니 오류가 발생했음
# 무조건 해줘야 됨
queue = deque()

# 각 번호에 이어지는 번호를 담을 리스트 생성
# ex. [[], [], [], []...] 
l = [[] for _ in range(N + 1)]

# 각 번호에 맞는 번호를 집어 넣음
for _ in range(M):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

# 이중 리스트 안에 있는 원소들을 오름차순으로 정렬
for i in range(N + 1):
    l[i].sort()

# DFS 방식(한 곳으로 쭈욱 들어가는 방식)
def dfs(node, visited):
    visited[node] = 1
    print(node, end = ' ')

    # 연결된 노드가 아직 방문하지 않은 곳이라면
    # 재귀 함수에 넣음(반복)
    for neibor in l[node]:    
        if visited[neibor] == 0:
            dfs(neibor, visited) 

# BFS 방식(인접한 원소를 모두 탐색하는 방식)
def bfs(start):
    visited = [0] * (N + 1)
    queue.append(start)
    visited[start] = 1

    # 큐 원소가 존재할 동안 계속 반복
    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        # 인접한 원소가 방문하지 않은 곳이라면
        # 방문에 체크하고 큐에 다시 집어 넣음
        for neibor in l[node]:
            if visited[neibor] == 0:
                visited[neibor] = 1
                queue.append(neibor)

# DFS 먼저 실행
visited_dfs = [0] * (N + 1)
dfs(V, visited_dfs)

print()

# 그 다음 BFS 실행
bfs(V)