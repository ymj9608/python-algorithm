from collections import Counter

N = int(input())

num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)

num_count = Counter(num_list)
most_num_sorted = sorted(num_count.items(), key=lambda x:(-x[1], x[0]))

print(most_num_sorted[0][0])