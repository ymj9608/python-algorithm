from collections import deque

N, K = map(int,input().split())

queue = deque(range(1, N+1))


result = []

while queue:
    # k-1 번 회전시켜 k 번째 사람을 맨 앞으로 보냅니다.
    # rotate의 인수가 음수이면 왼쪽으로 횐전합니다.
    queue.rotate(-(K-1))

    result.append(queue.popleft())

print("<"+", ".join(map(str,result))+">")