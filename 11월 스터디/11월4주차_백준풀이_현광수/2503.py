N = int(input())

count = 0
hints = [list(map(int, input().split())) for _ in range(N)]

for i in range(123, 988):
    comp_num = str(i)
    is_right = True

    if '0' in comp_num or len(set(comp_num)) != 3:
        continue

    is_valid = True
    for (num, strike, ball) in hints:
        origin_num = str(num)
        comp_strike = 0
        comp_ball = 0

        for j in range(3):
            if origin_num[j] == comp_num[j]:
                comp_strike += 1
            elif origin_num[j] in comp_num:
                comp_ball += 1

        if comp_strike != strike or comp_ball != ball:
            is_valid = False
            break

    if is_valid:
        count += 1

print(count)
