from collections import deque


def find_island(start_x, start_y, Map, visited):
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        for d in range(8):
            nx = x + deltas[d][0]
            ny = y + deltas[d][1]

            if 0 <= nx < w and 0 <= ny < h:
                if Map[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    map_list = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    is_Island = 0

    deltas = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for i in range(w):
        for j in range(h):

            if map_list[j][i] == 1 and not visited[j][i]:
                is_Island += 1
                find_island(i, j, map_list, visited)

    print(is_Island)