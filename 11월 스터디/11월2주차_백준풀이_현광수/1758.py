N = int(int(input()))

tip_list = []
for _ in range(N):
    tip = int(input())
    tip_list.append(tip)

tip_list.sort(reverse=True)
for i in range(len(tip_list)):
    tip_list[i] -= i
    if tip_list[i] < 0:
        tip_list[i] = 0

print(sum(tip_list))