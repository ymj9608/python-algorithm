N = int(input())
counting = {}
max_num = 0
max_count = 0
for _ in range(N):
    number = int(input())
    if number in counting:
        counting[number] += 1
    else:
        counting[number] = 1

    if counting[number] > max_count:
        max_num = number
        max_count = counting[number]
    elif counting[number] == max_count and number < max_num:
        max_num = number

print(max_num)