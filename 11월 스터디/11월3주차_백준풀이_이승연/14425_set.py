N, M = map(int, input().split())
sset = set([input() for _ in range(N)])

cnt = 0
for _ in range(M):
    sett = input()
    if sett in sset:
        count += 1

print(cnt)