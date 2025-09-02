# 숨바꼭질(BFS)
from collections import deque
N, K = map(int, input().split())

# 방문 여부를 체크할 리스트
visited = [0] * 100001

queue = deque()
# 시작 위치부터 넣기
queue.append(N)

while queue:
    current = queue.popleft()
    # 도착 위치에 오면 시간 출력하고 break
    if current == K:
        print(visited[current])
        break

    # 이동 가능한 범위 3가지    
    for next_loc in [current - 1, current + 1, current * 2]:
        # 범위를 벗어나지 않고 방문하지 않으면 탐색
        if 0 <= next_loc <= 100000 and visited[next_loc] == 0:
            # 다음 장소에 오면 현재 장소에서 1초 추가
            visited[next_loc] = visited[current] + 1
            queue.append(next_loc)