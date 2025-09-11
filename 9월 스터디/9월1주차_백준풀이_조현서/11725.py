# 트리의 부모 찾기
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 배열 생성
graph = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)  # 부모 저장 배열
q = deque([1])        # 루트 1번부터 시작

while q:
    current = q.popleft()
    # 현재 위치랑 연결된 부모 위치 확인
    for next in graph[current]:
        if parent[nxt] == 0:     # 아직 부모가 없으면
            parent[next] = current    # 부모를 기록
            q.append(next)

# 2번부터 N번까지 출력
for i in range(2, n+1):
    print(parent[i])
