move_dict = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1],
    }

king, stone, N = map(str, input().split())
times = int(N)

king_x = ord(king[0])
king_y = int(king[1])
stone_x = ord(stone[0])
stone_y = int(stone[1])

for _ in range(times):
    order = input()

    king_dx = king_x + move_dict[order][0]
    king_dy = king_y + move_dict[order][1]

    if 65 <= king_dx <= 72 and 1 <= king_dy <= 8:
        if king_dx == stone_x and king_dy == stone_y:
            stone_dx = stone_x + move_dict[order][0]
            stone_dy = stone_y + move_dict[order][1]
            if 65 <= stone_dx <= 72 and 1 <= stone_dy <= 8:
                king_x = king_dx
                king_y = king_dy
                stone_x = stone_dx
                stone_y = stone_dy
        else:
            king_x = king_dx
            king_y = king_dy

print(chr(king_x) + str(king_y))
print(chr(stone_x) + str(stone_y))