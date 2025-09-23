import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

q = deque([(B, 1)])
is_possible = False

# B를 A로 만드는 bfs
# 아이디어: B가 3, 5, 7, 9이면 A에 2를 곱하거나 1을 붙여서 만들 수 없음.
# A에 2를 곱하면 A는 짝수가 되므로 B의 일의 자리가 3, 5, 7, 9일 수 없음
# 따라서 B의 일의 자리 수가 1이거나 짝수여야함.
# 이때 B의 일의자리 수가 1이면 1을 빼는 연산. 예를 들어 841을 84로 만든다.
# B의 일의자리 수가 짝수이면 2로 나누는 연산. 예를 들어 840 > 420
# 위의 과정을 BFS
while q:
    now, count = q.popleft()

    if now == A:
        print(count)
        is_possible = True
        break

    # 1의 자리가 1이면 1을 제거하기
    if now % 10 == 1:
        next_num = now // 10
        if next_num >= A:
            q.append((next_num, count + 1))

    # 짝수이면 2로 나누기
    if now % 2 == 0:
        next_num = now // 2
        if next_num >= A:
            q.append((next_num, count + 1))


# 못찾았으면 -1 출력
if is_possible is False:
    print(-1)