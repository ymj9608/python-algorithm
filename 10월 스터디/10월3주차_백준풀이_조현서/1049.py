# 기타줄
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

min_pack = 1e9
min_piece = 1e9

# 기타줄 브랜드 개수만큼
# 패키지와 낱개 가격이 제시됨
for _ in range(M):
    package, piece = map(int, input().split())

    # 제일 싼 패키지, 낱개 가격을 미리 정함
    min_pack = min(min_pack, package)
    min_piece = min(min_piece, piece)


# 1. 전부 낱개 가격
all_piece = min_piece * N

# 2. 패키지는 패키지, 낱개는 낱개 가격
combo = (N // 6) * min_pack + (N % 6) * min_piece

# 3. 전부 패키지 가격
if N % 6 == 0:
    packs = N // 6
else:
    packs = N // 6 + 1

all_pack = packs * min_pack

# 가격 중 최솟값 출력
print(min(all_piece, combo ,all_pack))