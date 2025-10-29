N, M = map(int, input().split())

bundle_list = []
each_list = []
for _ in range(M):
    # bundle: 6개, each: 1개
    bundle, each = map(int, input().split())
    bundle_list.append(bundle)
    each_list.append(each)

bundle_min = min(bundle_list)
each_min = min(each_list)

min_price = min(((N // 6) + 1) * bundle_min, (N // 6) * bundle_min + (N % 6) * each_min, N * each_min )

print(min_price)