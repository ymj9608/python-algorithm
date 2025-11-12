# 촌수 계산
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
person1, person2 = map(int, input().split())
m = int(input())

relation = [[] for _ in range(n + 1)]

# 부모와 자식 관계를 양방향으로 저장
for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

# BFS
q = deque([(person1, 0)])
visited = [False] * (n + 1)
# 시작점 방문 처리
visited[person1] = True 

# 기본값 -1로 설정
result = -1  

while q:
    current, count = q.popleft()

    # person2와 같아지면 출력
    if current == person2:
        print(count)
        break

    # 연결된 사람들을 탐색
    for next_p in relation[current]:
        if not visited[next_p]:
            visited[next_p] = True
            q.append((next_p, count + 1))

# 큐가 빌 때까지 못 찾으면 -1 출력
else:
    print(-1)