import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    idx = 0
    cnt = 0

    for i in range(N):
        while idx < M:
            # A[i] > B[idx]이면 A[i]는 B[idx]부터 끝까지 다 먹을 수 있음
            # 즉, idx부터 M-1번째까지 먹을 수 있으므로 cnt에 M - idx 더하기
            # 예를 들어 A = [8, 7, 3, 1, 1], B = [6, 3, 1]
            # A[0] = 8 > B[0] = 6이므로 A[0]은 B 모두를 먹을 수 있음
            # A[1] = 7 > B[0] = 6이므로 마찬가지로 A[1]도 B 모두를 먹을 수 있음
            # A[2] = 3 < B[0] = 6이므로 idx += 1
            # A[2] = 3 < B[1] = 3이므로 idx += 1
            # A[2] = 3 < B[2] = 1이므로 A[2]는 B[2] 이후로 다 먹을 수 있음
            if A[i] > B[idx]:
                cnt += M - idx
                break
            else:
                idx += 1

    print(cnt)