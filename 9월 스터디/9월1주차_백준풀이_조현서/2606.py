# 바이러스
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())      # 컴퓨터 수 
m = int(input())      # 연결 개수 

# 그래프 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 탐색
visited = [False] * (n + 1)
q = deque([1])     # 1번 컴퓨터부터
visited[1] = True

count = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)
            count += 1   # 새로 감염된 컴퓨터 수 증가

print(count)
