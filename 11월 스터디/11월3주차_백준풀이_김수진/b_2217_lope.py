N = int(input())
lopes = [int(input()) for _ in range(N)]

lopes.sort(reverse=True)
max_weight = lopes[0]

# 내가 선택한 로프들 중 가장 낮은 중량을 들 수 있는 로프의 무게와
# 내가 선택한 로프들 갯수를 곱한 것이
# 현재 내가 선택한 로프들로 들 수 있는 최대 중량이다.
for i in range(1, N):
    weight = lopes[i]*(i+1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)