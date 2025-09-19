# 뱀과 사다리 게임
'''
사다리 칸에 오면 현재 번호보다 커지고,
뱀 칸에 오면 현재 번호보다 작아짐
시작 : 1번 칸
끝: 100번 칸
주사위 굴려야 하는 횟수의 최솟값
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
jumps = [tuple(map(int, input().split())) for _ in range(N + M)]

visited = [0] * 101
q = deque([1])
visited[1] = 1

while q:
    current, count = q.popleft()
    # 100 칸에 오면
    # 현재까지의 카운트 출력
    if current == 100:
        print(count)
        break
    # 주사위 1 ~ 6
    for n in (1, 7):
        next_loc = current + n
        # 가지치기 : 다음 칸이 100칸을 넘으면 그냥 무시(고려 x)
        if next_loc > 100:
            continue

        # 뱀이나 사다리 칸이면
        if move[next_loc] != 0:
            # 해당하는 다음 칸으로 이동
            next_loc = move[next_loc]

        # 갔던 칸이 아니면 방문 처리
        if not visited[next_loc]:
            visited[next_loc] = 1
            q.append((next_loc, count + 1))