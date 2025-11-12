N = int(input())

length = 1 + 4 * (N - 1)

grid = [[' '] * length for _ in range(length)]

def draw_star(n, r, c):
    if n == 1:
        grid[r][c] = '*'
        return
    else:
        current_len = 1 + 4 * (n - 1)
        for i in range(current_len):
            grid[r][c + i] = '*'
            grid[r + current_len - 1][c + i] = '*'
            grid[r + i][c] = '*'
            grid[r + i][c + current_len - 1] = '*'

    draw_star(n - 1, r + 2, c + 2)
draw_star(N, 0 ,0)
for row in grid:
    print("".join(row))