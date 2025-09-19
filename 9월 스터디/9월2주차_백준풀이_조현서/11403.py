# 경로 찾기
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * N for _ in range(N)]

for start in range(N):
    visited = [0] * N
    stack = [start]

    while stack:
        now = stack.pop()
        # 오른쪽으로 가면서
        for next_loc in range(N):
            # 경로가 있고 방문하지 않은 곳이라면
            if arr[now][next_loc] == 1 and visited[next_loc] == 0:
                # 방문 처리
                visited[next_loc] = 1
                stack.append(next_loc)
    for i in range(N):
        if visited[i]:
            result[start][i] = 1

for row in result:
    print(*row)