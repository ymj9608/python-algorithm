import sys
input = sys.stdin.readline

N, M = map(int, input().split())

min_package_price = float('inf')
min_each_price = float('inf')
for _ in range(M):
    package_price, each_price = map(int, input().split())

    # 패키지 최소 가격, 낱개 최소 가격 갱신
    min_package_price = min(min_package_price, package_price)
    min_each_price = min(min_each_price, each_price)

# 필요한 패키지 수
need_package = N // 6

# 필요한 낱개 수
need_each = N % 6

# (패키지 최소 가격)과 (낱개 최소 가격 * 6)을 비교
if min_package_price > min_each_price * 6:
    total_price = N * min_each_price
    print(total_price)
# 패키지가 더 쌀 경우, 낱개 처리를 위해 (패키지 1개의 가격), (낱개 * 낱개 최소 가격)을 비교
elif min_package_price >= need_each * min_each_price:
    total_price = need_package * min_package_price + need_each * min_each_price
    print(total_price)
else:
    total_price = (need_package + 1) * min_package_price
    print(total_price)