# 최소 비용 구하기
'''
다익스트라 함수 활용 연습
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 도시의 개수만큼 경로 배열 생성
routes = [[] for _ in range(N + 1)]

# 버스의 개수만큼 비용과 출발도시, 도착 도시 주어짐
for _ in range(M):
    start_city, end_city, cost = map(int, input().split())
    # 비용과 도착 도시를 튜플로 출발 도시 경로에 집어넣음
    routes[start_city].append((cost, end_city))

start, end = map(int, input().split())

INF = float('inf')
min_cost = [INF] * (N + 1)
min_cost[start] = 0

pq = [(0, start)]

while pq:
    # (누적비용, 현재도시)
    # 출발점부터 시작
    total_cost, city = heappop(pq)   

    # 가지치기 : 꺼낸 비용이 이미 최솟값보다 크면 넘어감
    if total_cost > min_cost[city]:
        continue

    # 도착하면 총비용 출력(종료)
    if city == end:
        print(total_cost)
        break

    for cost, next_city in routes[city]:
        new_cost = total_cost + cost
        # 최솟값 갱신
        if new_cost < min_cost[next_city]:
            min_cost[next_city] = new_cost
            # 갱신 후 최솟값과 다음 도시 집어넣음
            heappush(pq, (new_cost, next_city)) 