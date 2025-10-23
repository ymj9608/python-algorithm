from collections import deque

N = int(input())
balloon = list(map(int, input().split()))

queue = deque()
answer = []

for i in range(N):
    queue.append((i + 1, balloon[i]))

first_seq, first_score = queue.popleft()
answer.append(first_seq)
start = first_score

while queue:
    if start > 0:
        queue.rotate(1 - start)
    else:
        queue.rotate(abs(start))

    seq, score = queue.popleft()
    answer.append(seq)
    start = score

print(*answer)
