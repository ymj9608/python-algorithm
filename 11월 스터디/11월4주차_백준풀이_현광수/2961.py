from itertools import combinations

N = int(input())

Yori = float('inf')
Yori_list = []
for _ in range(N):
    Syeo, SSeo = map(int, input().split())
    Yori_list.append((Syeo, SSeo))

for i in range(1, N + 1):
    comb = combinations(Yori_list, i)

    for each_team in comb:
        comp_Syeo = 1
        comp_SSeo = 0
        for Syeo, SSeo in each_team:
            comp_Syeo *= Syeo
            comp_SSeo += SSeo

        total = abs(comp_SSeo - comp_Syeo)

        if total < Yori:
            Yori = total

print(Yori)
