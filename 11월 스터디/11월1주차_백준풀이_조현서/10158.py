# 개미
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 기본 이동 방향(대각선 오른쪽 위)
dx = [1, 1, -1, 1]
dy = [1, -1, -1, 1]

arr = [[0] * (w + 1) for _ in range(h + 1)]
print(arr)

# 현재 위치
current = arr[p][q]

for _ in range(t):
