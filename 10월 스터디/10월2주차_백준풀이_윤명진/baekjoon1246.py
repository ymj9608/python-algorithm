import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pi_list = [int(input()) for _ in range(M)]
min_price = float('inf')
max_total_price = 0

for price in pi_list:
    # price로 책정했을 때, 살 수 있는 사람의 수
    people = 0

    for i in range(M):
        if pi_list[i] >= price:
            people += 1
        # 최대 N개까지만 판매 가능
        if people == N:
            break

    # 수익이 최대이면 모든 값 갱신 (등호를 포함하지 않은 이유는 수익이 최대인 것 중 달걀의 최솟값을 구해야 하기 때문)
    if max_total_price < price * people:
        max_total_price = price * people
        min_price = price


print(min_price, max_total_price)