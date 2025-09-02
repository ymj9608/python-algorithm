import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

# 인접리스트 생성
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


parent = [0] * (N + 1)

q = deque([1])

# bfs로 구현
while q:
    p = q.popleft()

    # 현재 노드와 연결된 모든 자식 노드 확인
    for child in graph[p]:
        # 방문하지 않았으면
        if parent[child] == 0:
            # 현재 노드를 부모로 기록
            parent[child] = p
            # 다음 탐색을 위해 큐에 추가
            q.append(child)

# 2번 노드부터 N번 노드까지의 부모를 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])