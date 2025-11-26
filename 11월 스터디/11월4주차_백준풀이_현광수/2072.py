import sys

N = int(input())
board = [[0 for _ in range(19)] for _ in range(19)]


def checkwin(r, c, Color, board):
    deltas = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)], [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    for each_dir in deltas:
        count = 1

        for dir in each_dir:
            nr = r + dir[0]
            nc = c + dir[1]

            while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == Color:
                count += 1
                nr += dir[0]
                nc += dir[1]

        if count == 5:
            return True
    return False


for turn in range(N):
    x, y = map(int,input().split())
    x -= 1
    y -= 1

    if turn % 2 != 0:
        color = 2
    else:
        color = 1

    board[x][y] = color

    if checkwin(x, y, color, board):
        print(turn + 1)
        sys.exit(0)

print(-1)