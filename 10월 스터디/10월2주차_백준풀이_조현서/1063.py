# 킹
'''
아스키 함수를 사용해 문자열을 좌표로 바꾸고
다시 문자열로 바꾸기
'''
import sys
input = sys.stdin.readline

# 방향 딕셔너리 설정
moves = {
    'R':(0, 1),
    'L':(0, -1),
    'B':(-1, 0),
    'T':(1, 0),
    'RT':(1, 1),
    'LT':(1, -1),
    'RB':(-1, 1),
    'LB':(-1, -1)
}
# 문자열을 좌표로 바꾸는 함수
def str_to_coord(str):
    col = ord(str[0]) - ord('A') + 1
    row = int(str[1])
    return (row, col)

# 좌표를 다시 문자열로 바꾸는 함수
def coord_to_str(row, col):
    return chr(col + ord('A') -1) + str(row)

K, R, N = map(str, input().split())
N = int(N)

# 왕과 돌의 위치를 좌표로 바꿈
kx, ky = str_to_coord(K)
rx, ry = str_to_coord(R)

for _ in range(N):
    cmd = input().strip()
    dx, dy = moves[cmd]

    # 일단 왕 위치 이동
    nkx = kx + dx
    nky = ky + dy
    # 범위 내만 고려
    if 1 <= nkx <= 8 and 1 <= nky <= 8:
        # 돌 위치랑 겹치면
        if nkx == rx and nky == ry:
            # 돌도 왕이 이동한 방향으로 이동시킴
            nrx = rx + dx
            nry = ry + dy
            # 돌도 범위 내만 고려
            if 1 <= nrx <= 8 and 1 <= nry <= 8:
                kx, ky = nkx, nky
                rx, ry = nrx, nry

        # 돌이랑 안 겹치면 왕만 이동
        else:
            kx, ky = nkx, nky

print(coord_to_str(kx, ky))
print(coord_to_str(rx, ry))