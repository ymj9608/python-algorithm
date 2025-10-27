N, M = map(int, input().split())

board = [input() for _ in range(N)]

min_repaints = 64

# 8X8 순회하면서 체크해보기
for start_row in range(N - 7):
    for start_col in range(M - 7):

        repaint_w = 0
        repaint_b = 0

        for r in range(8):
            for c in range(8):
                current_r, current_c = start_row + r, start_col + c

                # 좌우 번갈아가면서 BWBW 혹은 WBWB로 가야하므로 인덱스를 2로 나눈 나머지를 활용
                if (r + c) % 2 == 0:
                    if board[current_r][current_c] != 'W':
                        repaint_w += 1
                else:
                    if board[current_r][current_c] != 'B':
                        repaint_w += 1

                if (r + c) % 2 == 0:
                    if board[current_r][current_c] != 'B':
                        repaint_b += 1
                else:
                    if board[current_r][current_c] != 'W':
                        repaint_b += 1

        min_repaints = min(min_repaints, repaint_w, repaint_b)

print(min_repaints)