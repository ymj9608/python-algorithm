from collections import deque

subin, brother = map(int, input().split())

# 방문처리할 visited 생성
visited = [0] * 100001

# bfs로 구현
def bfs(s, b):
    # 수빈이와 동생의 위치가 같다면 0 반환
    if s == b:
        return 0

    # 시작점 큐에 넣고 방문처리
    q = deque([[s, 0]])
    visited[s] = 1

    # q에 저장된 현재 위치와 시간 꺼내기
    while q:
        now, seconds = q.popleft()

        # 현재 위치에서 1 더하기, 1 빼기, 2 곱하기 탐색
        for next_pos in (now - 1, now + 1, now * 2):
            # 다음 위치가 b이면 second에 1 더하고 반환
            if next_pos == b:
                return seconds + 1

            # 다음 위치가 범위 내에 있으며 방문하지 않았다면 q에 추가하고, 방문처리
            if 0 <= next_pos <= 100000 and visited[next_pos] == 0:
                q.append([next_pos, seconds + 1])
                visited[next_pos] = 1


result = bfs(subin, brother)
print(result)