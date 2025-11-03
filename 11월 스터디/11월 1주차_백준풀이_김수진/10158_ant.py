w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

# 우상, 좌상, 좌하, 우하
dir = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

np = p
nq = q
d = 0

for t in range(T):
    # 오른쪽 벽에 부딪혔을 때
    if np == w:
        d = 1
        if nq == h:
            d = 2
    elif nq == h:
        d = 2
        if np == 0:
            d = 3
    elif np == 0:
        d = 0
    elif nq == 0:
        d = 1

    np += dir[d][0]
    nq += dir[d][1]

print(np, nq)