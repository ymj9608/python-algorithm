N, M = map(int, input().split())

trees = list(map(int, input().split()))

# 시작을 1, 마지막을 가장 큰 나무의 높이로 세팅
start = 1
end = max(trees)

# 이분 탐색 시작
while start <= end:
    sums = 0
    mid = (start+end)//2

    for height in trees:
        if height > mid:
            sums += height - mid

    # start = mid + 1, end = mid - 1로 잡은 이유
    # 예를 들어 N = 3 M = 2, trees = [100, 100, 100]이면
    # 첫번째 start = 1, end = 100, mid = 50 > 얻은 목재 150
    # 두번째 start = 51, end = 100, mid = 75 > 얻은 목재 75
    # 세번째 start = 76, end = 100, mid = 88 > 얻은 목재 36
    # 네번째 start = 89, end = 100, mid = 94 > 얻은 목재 18
    # 다섯번째 start = 95, end = 100, mid = 97 > 얻은 목재 9
    # 여섯번째 start = 98, end = 100, mid = 99 > 얻은 목재 3
    # 일곱번째 start = 100, end = 100, mid = 100 > 얻은 목재 0
    # 여덟번째 start = 100, end = 99 > while문 종료 < 최종 end값은 99
    # 즉, M보다는 계속 크다가, M보다 작아지는 순간 그때의 mid - 1 값이 최대 높이임
    # 위의 케이스에서 필요한 목재는 2이지만 정확히 2를 못얻으므로 3을 얻어야 함.
    if sums >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)