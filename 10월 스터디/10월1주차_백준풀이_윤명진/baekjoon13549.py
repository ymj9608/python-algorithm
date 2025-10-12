from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([N])
visited = [-1] * 100001
visited[N] = 0

# BFS
while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break
    
    # 순간이동 우선 탐색 (다음 popleft도 순간이동부터 꺼내지기 위해 q의 가장 왼쪽에 추가)
    if 0 <= now * 2 <= 100000 and visited[now * 2] == -1:
        visited[now * 2] = visited[now]
        q.appendleft(now * 2)

    # 이후 -1, +1 연산 탐색
    if 0 <= now - 1 <= 100000 and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)

    if 0 <= now + 1 <= 100000 and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)