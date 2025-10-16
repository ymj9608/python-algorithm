from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))
a, b = map(int, input().split())
# 인덱스와 징검다리 번호 맞추기
a -= 1
b -= 1

q = deque([a])
visited = [-1] * 10001
visited[a] = 0
is_able = False

while q:
    now = q.popleft()

    if now == b:
        print(visited[now])
        is_able = True
        break

    # stones[now]의 배수만큼 점프 가능
    for jump in range(stones[now], N + 1, stones[now]):
        # 앞으로 점프
        next_stone = now + jump
        if 0 <= next_stone < N and visited[next_stone] == -1:
            visited[next_stone] = visited[now] + 1
            q.append(next_stone)

        # 뒤로 점프
        back_next_stone = now - jump
        if 0 <= back_next_stone < N and visited[back_next_stone] == -1:
            visited[back_next_stone] = visited[now] + 1
            q.append(back_next_stone)

if not is_able:
    print(-1)
