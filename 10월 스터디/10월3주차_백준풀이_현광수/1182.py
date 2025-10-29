from itertools import combinations

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
all_sums = []

for i in range(1, N + 1):
    comb_sums = [sum(combo) for combo in combinations(num_list,i)]
    all_sums.extend(comb_sums)

print(all_sums.count(S))