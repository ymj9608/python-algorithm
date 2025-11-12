from collections import Counter

N = int(input())
sim_cnt = 0

std_word = input()
base_cnt = Counter(std_word)

for _ in range(N - 1):
    compare_word = input()
    compare_cnt = Counter(compare_word)

    diff1 = base_cnt - compare_cnt
    diff2 = compare_cnt - base_cnt

    added_cnt = sum(diff1.values())
    removed_cnt = sum(diff2.values())

    if added_cnt < 2 and removed_cnt < 2:
        sim_cnt += 1

print(sim_cnt)