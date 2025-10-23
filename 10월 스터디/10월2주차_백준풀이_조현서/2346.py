# 풍선 터뜨리기
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))

# (인덱스, 값)의 형태로 담음
q = deque(enumerate(balloons, 1))

result = []
while q:
    idx, move = q.popleft()
    result.append(idx)

    # 종료 조건을 안 넣으면 에러가 뜸
    # 마지막 원소를 꺼냈을 때 다음 if문을 들어가면서 에러
    if not q:
        break

    # 양수일 경우 오른쪽으로 이동
    # 왼쪽에서 꺼내서 오른쪽으로 이동시킴
    if move > 0:
        # -1을 안했더니 (5, -1)이 출력됨
        for _ in range(move - 1):
            q.append(q.popleft())

    # 음수일 경우 왼쪽으로 이동
    else:
        for _ in range(-move):
            # 오른쪽에서 꺼내서 왼쪽으로 이동시킴
            q.appendleft(q.pop())

    # print(q)
print(*result)