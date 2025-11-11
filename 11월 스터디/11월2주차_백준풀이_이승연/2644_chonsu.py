from collections import deque
N = int(input())
x, y = map(int, input().split())
m = int(input())
arr = []
for _ in range(m):
    rel = list(map(int, input().split()))
    arr.append(rel)
    
graph = [[] for _ in range(N+1)]
for a, b in arr:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
dist = [0] * (N+1)

# 우리가 아는 큐를 이용한 BFS 코드
q = deque([x])
visited[x] = True

while q:
    now = q.popleft()
    if now == y:
        print(dist[now])
        break
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            # 이웃 노드의 거리를 현재 노드의 거리 +1로 생각
            dist[nxt] = dist[now] + 1
            q.append(nxt)
else:
    print(-1)