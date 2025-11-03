N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

blocks.sort()

space = 0
width = blocks[0][0]
height = blocks[0][1]
for i in range(1, N-1):
    if height <= blocks[i][1]:
        space += (blocks[i][0] - width) * height
    else:

