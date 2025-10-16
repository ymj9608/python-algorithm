import sys
input = sys.stdin.readline

N = int(input())
balloons_input = list(map(int, input().split()))

# 풍선 번호와 인덱스 맞추기
balloons = list(enumerate(balloons_input, 1))
result = []
idx = 0

while balloons:
    original_idx, move = balloons.pop(idx)
    result.append(original_idx)

    # 풍선 전부 터뜨리면 종료
    if not balloons:
        break
    
    # 풍선에 적힌 수가 양수일 때
    if move > 0:
        idx = (idx + move - 1) % len(balloons)
    # 음수일 때
    else:
        idx = (idx + move) % len(balloons)

print(*result)