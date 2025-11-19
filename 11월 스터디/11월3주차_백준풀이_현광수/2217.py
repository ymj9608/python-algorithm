N = int(input())

weight_list = []
for _ in range(N):
    rope = int(input())
    weight_list.append(rope)

max_weight = 0
weight_list.sort()

for i in range(N):
    if max_weight < (weight_list[i] * (N - i)):
        max_weight = weight_list[i] * (N - i)

print(max_weight)