from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
first_person, second_person = map(int, input().split())

m = int(input())
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())

    # x가 부모, y가 자식 (양방향)
    adj_list[x].append(y)
    adj_list[y].append(x)

q = deque([(first_person, 0)])
visited = [0] * (n+1)
is_cousin = False
chon_cnt = 100

# BFS
while q:
    now_person, cnt = q.popleft()

    
    if now_person == second_person:
        chon_cnt = min(chon_cnt, cnt)
        is_cousin = True

    # 인접 촌수 계산
    for next_person in adj_list[now_person]:
        if visited[next_person] == 0:
            visited[next_person] = 1
            q.append((next_person, cnt + 1))

if is_cousin:
    print(chon_cnt)
else:
    print(-1)