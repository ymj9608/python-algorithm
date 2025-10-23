from collections import deque

N = int(input())

bridge = list(map(int, input().split()))
a, b = map(int, input().split())

queue = deque()
visited = [False for _ in range(N + 1)]
visited[a] = True
queue.append((a, 0))
answer = -1

while queue:
    curr_pos, jump_cnt = queue.popleft()

    if curr_pos == b:
        answer = jump_cnt
        break
    else:
        for k in range(1, N):
            next_pos = curr_pos + k * bridge[curr_pos - 1]
            if next_pos > N:
                break
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jump_cnt + 1))

        for q in range(1, N):
            next_pos = curr_pos - q * bridge[curr_pos - 1]
            if next_pos < 1:
                break
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jump_cnt + 1))


print(answer)