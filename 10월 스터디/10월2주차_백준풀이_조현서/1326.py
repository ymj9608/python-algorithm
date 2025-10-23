# 폴짝폴짝
'''
방문하면서 + 1씩 해줘야 한다.
앞으로 갈수도, 뒤로 갈수도 있음
bfs 방식을 이용
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
# 인덱스와 징검다리 번호와 맞춰주기 위함
rocks = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

# 방문 처리 배열(갈 수 없는 경우엔 -1이 출력되야 하므로 -1 기본값)
visited = [-1] * (N + 1)
q = deque([a])
visited[a] = 0

while q:
    now = q.popleft()
    jump = rocks[now]
    
    # 앞으로 점프
    # 1배수부터 점차 늘려나감
    k = 1
    while True:
        nxt = now + k * jump
        # 범위를 넘어가면 종료
        if nxt > N:
            break
        # 범위 안이면 방문 처리 및 점프 이동
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            q.append(nxt)
        k += 1

    # 뒤로 점프
    # 마찬가지
    k = -1
    while True:
        nxt = now + k * jump
        # 징검다리는 1부터 시작이므로 1보다 작아지면 종료
        if nxt < 1:
            break

        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            q.append(nxt)
        k -= 1

# 목적지(b)까지 얼마나 걸렸는지 출력 
print(visited[b])