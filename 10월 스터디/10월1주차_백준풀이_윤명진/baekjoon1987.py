import sys
input = sys.stdin.readline

# 백트래킹 구현
def find_route(i, j, count):
    global max_count
    max_count = max(max_count, count)

    # 델타 탐색
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            # 인접한 구역의 알파벳 인덱스 > 같은 알파벳이 있으면 안되므로 방문 안한 곳만 탐색
            next_alpha_idx = ord(alphabet[ni][nj]) - ord('A')
            if not visited[next_alpha_idx]:
                visited[next_alpha_idx] = True
                find_route(ni, nj, count + 1)
                visited[next_alpha_idx] = False

R, C = map(int, input().split())
alphabet = [input().rstrip() for _ in range(R)]

visited = [False] * 26
max_count = 1

start_alpha_idx = ord(alphabet[0][0]) - ord('A')
visited[start_alpha_idx] = True
find_route(0, 0, 1)

print(max_count)