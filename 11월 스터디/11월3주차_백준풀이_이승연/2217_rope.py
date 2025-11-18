import sys
input = sys.stdin.readline
N = int(input())
weight = [int(input()) for _ in range(n)]

# 내림차순으로 정렬
weight.sort(reverse = True)
max_weight = 0

for i in range(len(weight)):
  # i+1번째에는 i+1만큼의 가중치가 부여되는것과 같음
  new_weight = weight[i] * (i+1)

  # 들어올릴 수 있는 최대 중량 업데이트
  if new_weight > max_weight:
    max_weight = new_weight

print(max_weight)