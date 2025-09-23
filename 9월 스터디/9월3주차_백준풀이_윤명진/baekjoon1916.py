from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 인접리스트 생성
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    start_bus_stop, end_bus_stop, bus_cost = map(int, input().split())
    adj_list[start_bus_stop].append((bus_cost, end_bus_stop))

start, end = map(int, input().split())

# 우선순위큐
pq = [(0, start)]
costs = [float('inf')] * (N + 1)


while pq:
    cost, now_bus_stop = heappop(pq)

    # 도착점에 도착했다면 비용 출력
    if now_bus_stop == end:
        print(cost)
        break
    
    # 지금 정류장에 도착할 수 있는 최소비용보다 커지면 다음 탐색
    if cost > costs[now_bus_stop]:
        continue
    
    # 다음 정류장 탐색 인접 리스트에는 (비용, 정류장) 튜플 형태로 담겨 있음
    for next_cost, next_bus_stop in adj_list[now_bus_stop]:
        new_cost = cost + next_cost

        # 지금까지의 비용 + 다음 정류장까지의 비용이 이미 저장된 다음 정류장까지의 최소비용보다
        # 크면 탐색할 필요 없음
        if new_cost >= costs[next_bus_stop]:
            continue
        
        # 다음 정류장까지의 최소비용 갱신
        costs[next_bus_stop] = new_cost
        heappush(pq, (new_cost, next_bus_stop))