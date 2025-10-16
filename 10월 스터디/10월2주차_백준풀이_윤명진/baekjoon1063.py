import sys
input = sys.stdin.readline

king, stone, N = input().rstrip().split()
N = int(N)
king_location = list(king)
stone_location = list(stone)
king_location[1] = int(king_location[1])
stone_location[1] = int(stone_location[1])

for _ in range(N):
    command = input().rstrip()

    # R: 한칸 오른쪽으로 (오른쪽 좌표는 h까지)
    if command == 'R' and ord(king_location[0]) < ord('H'):
        king_location[0] = chr(ord(king_location[0]) + 1)
        # 그런데 오른쪽에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) + 1)
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) > ord('H'):
                king_location[0] = chr(ord(king_location[0]) - 1)
                stone_location[0] = chr(ord(stone_location[0]) - 1)

    # L: 한칸 왼쪽으로 (왼쪽 좌표는 a까지)
    elif command == 'L' and ord(king_location[0]) > ord('A'):
        king_location[0] = chr(ord(king_location[0]) - 1)
        # 그런데 왼쪽에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) - 1)
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) < ord('A'):
                king_location[0] = chr(ord(king_location[0]) + 1)
                stone_location[0] = chr(ord(stone_location[0]) + 1)

    # B: 한칸 아래로 (아래 좌표는 1까지)
    elif command == 'B' and king_location[1] > 1:
        king_location[1] -= 1
        # 그런데 아래에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[1] -= 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if stone_location[1] < 1:
                king_location[1] += 1
                stone_location[1] += 1

    # T: 한칸 위로 (위 좌표는 8까지)
    elif command == 'T' and king_location[1] < 8:
        king_location[1] += 1
        # 그런데 아래에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[1] += 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if stone_location[1] > 8:
                king_location[1] -= 1
                stone_location[1] -= 1

    # RT: 오른쪽 위 대각선으로
    elif command == 'RT' and ord(king_location[0]) < ord('H') and king_location[1] < 8:
        king_location[0] = chr(ord(king_location[0]) + 1)
        king_location[1] += 1
        # 그런데 오른쪽 위 대각선에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) + 1)
            stone_location[1] += 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) > ord('H') or stone_location[1] > 8:
                king_location[0] = chr(ord(king_location[0]) - 1)
                king_location[1] -= 1
                stone_location[0] = chr(ord(stone_location[0]) - 1)
                stone_location[1] -= 1

    # LT: 왼쪽 위 대각선으로
    elif command == 'LT' and ord(king_location[0]) > ord('A') and king_location[1] < 8:
        king_location[0] = chr(ord(king_location[0]) - 1)
        king_location[1] += 1
        # 그런데 오른쪽 위 대각선에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) - 1)
            stone_location[1] += 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) < ord('A') or stone_location[1] > 8:
                king_location[0] = chr(ord(king_location[0]) + 1)
                king_location[1] -= 1
                stone_location[0] = chr(ord(stone_location[0]) + 1)
                stone_location[1] -= 1

    # RB: 오른쪽 아래 대각선으로
    elif command == 'RB' and ord(king_location[0]) < ord('H') and king_location[1] > 1:
        king_location[0] = chr(ord(king_location[0]) + 1)
        king_location[1] -= 1
        # 그런데 오른쪽 위 대각선에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) + 1)
            stone_location[1] -= 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) > ord('H') or stone_location[1] < 1:
                king_location[0] = chr(ord(king_location[0]) - 1)
                king_location[1] += 1
                stone_location[0] = chr(ord(stone_location[0]) - 1)
                stone_location[1] += 1

    # LB: 왼쪽 아래 대각선으로
    elif command == 'LB' and ord(king_location[0]) > ord('A') and king_location[1] > 1:
        king_location[0] = chr(ord(king_location[0]) - 1)
        king_location[1] -= 1
        # 그런데 오른쪽 위 대각선에 돌이 있다면 돌도 움직이기
        if king_location == stone_location:
            stone_location[0] = chr(ord(stone_location[0]) - 1)
            stone_location[1] -= 1
            # 그런데 스톤이 범위를 벗어낫다면 전부 원상복구
            if ord(stone_location[0]) < ord('A') or stone_location[1] < 1:
                king_location[0] = chr(ord(king_location[0]) + 1)
                king_location[1] += 1
                stone_location[0] = chr(ord(stone_location[0]) + 1)
                stone_location[1] += 1


print("".join(map(str, king_location)))
print("".join(map(str, stone_location)))