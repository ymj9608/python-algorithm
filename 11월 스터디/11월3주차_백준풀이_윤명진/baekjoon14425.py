import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = {input().rstrip(): 0 for _ in range(N)}

cnt = 0
for _ in range(M):
    check_str = input().rstrip()
    # 딕셔너리 S에 있는지 확인
    if check_str in S:
        cnt += 1

print(cnt)