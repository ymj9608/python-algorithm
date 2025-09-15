from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

my_dict = {}

# 포털을 딕셔너리로 저장 (뱀, 사다리 구분할 필요 없음)
# 시작점 : key, 도착점 : value
for _ in range(N + M):
    x, y = map(int, input().split())
    my_dict[x] = y

# 1번부터 시작
q = deque([1])
visited = [0] * 101
visited[1] = 0


while q:
    now = q.popleft()
    
    # now가 처음으로 100이 되는 경우 최소 횟수는 visited[now]이므로 출력 후 반복문 종료
    if now == 100:
        print(visited[now])
        break

    for next_location in (now + 1, now + 2, now + 3, now + 4, now + 5, now + 6):
        # next_location이 포털의 시작점인 경우, 도착점으로 세팅
        if next_location in my_dict:
            next_location = my_dict[next_location]

        # next_location이 100이하이면서, 방문하지 않았다면 탐색
        if next_location <= 100 and visited[next_location] == 0:
            # visited에 next_location에 도달할 수 있는 최솟값이 저장됨.
            visited[next_location] = visited[now] + 1
            q.append(next_location)