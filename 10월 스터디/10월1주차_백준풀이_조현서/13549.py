# 숨바꼭질 3
'''
수빈이 선택지
1. 걷는다(x - 1, x + 1)
   1초 걸림
2. 순간이동(2 * x)
   0초 걸림
'''
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([N])

# N이 100000까지이므로 
visited = [-1] * 100001
visited[N] = 0

# BFS 탐색
while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break
    
    # 순간이동 우선 탐색
    # 범위 내에 있고 방문한 적 없으면 방문 처리
    if 0 <= now * 2 <= 100000 and visited[now * 2] == -1:
        # 0초 후에 이동이므로 그대로 
        visited[now * 2] = visited[now]
        q.append(now * 2)

    # 이후 -1, +1 이동 탐색
    # 걷는 건 1초 후에 이동이므로 + 1
    if 0 <= now - 1 <= 100000 and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)

    if 0 <= now + 1 <= 100000 and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)