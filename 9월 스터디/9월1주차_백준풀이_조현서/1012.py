# 유기농 배추
'''
배추끼리 인접해있으면 그 배추들은 해충으로부터 보호받음
배추의 상하좌우 네 방향에 다른 배추가 있으면 인접한 것
필요한 최소의 배추 흰 지렁이 마리 수를 출력
'''
import sys
input = sys.stdin.readline()

T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, input().split())

    # 배추의 위치를 채워넣을 배열 생성
    arr = [[0] * M for _ in range(N)]

    # 배추의 개수만큼 순회하면서
    # 각각의 배추 위치를 배열에 담음
    for _ in range(K):
        X, Y = map(int, input().split())
    print(X, Y)


