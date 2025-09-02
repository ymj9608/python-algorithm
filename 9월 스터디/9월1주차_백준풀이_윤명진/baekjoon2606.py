from collections import deque
N = int(input())
M = int(input())

# 그래프 입력
my_list = [list(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# 연결리스트 생성 (양방향)
for i, j in my_list:
    adj_list[i].append(j)
    adj_list[j].append(i)

# 1번부터 시작이므로 덱으로 저장
q = deque([1])
visited[1] = 1
count = 0

# bfs로 구현
while q:
    computer = q.popleft()

    # 인접 컴퓨터를 방문하지 않은 경우 감염된 컴퓨터 개수 1 늘리고 방문처리, q에 추가
    for next_computer in adj_list[computer]:
        if visited[next_computer] == 0:
            count += 1
            visited[next_computer] = 1
            q.append(next_computer)

print(count)