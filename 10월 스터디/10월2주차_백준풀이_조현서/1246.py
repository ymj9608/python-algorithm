# 온라인 판매
'''

'''
import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]

# 우선 낮은 가격부터 정렬
prices.sort()
best_profit = 0
best_price = 0

for i in range(M):
    price = prices[i]

    # 그 이상 지불가능한 사람 수
    buy = M - i
    # 판매가능한 계란 수
    sell = min(N, buy)
    profit = price * sell

    # 최대 이익 갱신
    if profit > best_profit:
        best_profit = profit
        # 최대 이익일때 가격이 베스트 
        best_price = price

print(best_price, best_profit)