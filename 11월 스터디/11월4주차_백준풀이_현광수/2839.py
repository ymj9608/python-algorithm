N = int(input())

dp = []

for i in range(N // 3 + 1):
    for j in range(N // 5 + 1):
        if 3 * i + 5 * j == N:
            dp.append(i + j)

if len(dp) == 0:
    print(-1)
else:
    print(min(dp))