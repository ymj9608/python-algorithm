from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

chicken_house = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))

        elif city[i][j] == 2:
            chicken_house.append((i, j))

# 치킨집들 중 M개 고르기
m_select = list(combinations(chicken_house, M))

city_chicken_distance = 1300

# 각 집마다 치킨집까지의 최소 거리 측정
# 각 경우의 수 별로, 치킨거리의 합을 구해야 함
for i in range(len(m_select)):
    total_sum = 0

    # 각 집마다 조사하기, 집마다 치킨집까지의 최소 거리 초기화
    for r, c in house:
        min_distance = 100
        # i번째 경우의 각 치킨집에 대해 최소 거리 계산 후 갱신
        for chickens in m_select[i]:
            distance = abs(chickens[0] - r) + abs(chickens[1] - c)
            min_distance = min(min_distance, distance)

        # 치킨집 전부 순회 후, 최솟값을 더해줌 (total_sum은 도시 치킨 거리)
        total_sum += min_distance

    # 각 경우의 수마다 도시 치킨 거리를 계산하여 최솟값 갱신
    city_chicken_distance = min(city_chicken_distance, total_sum)

print(city_chicken_distance)