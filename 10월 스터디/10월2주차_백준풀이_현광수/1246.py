N, M = map(int, input().split())

buyer_list = []

for _ in range(M):
    price = int(input())
    buyer_list.append(price)

max_profit = 0
max_price = 0

if N < M:
    tmp = M - N
    buyer_list.sort()
    buyer_list = buyer_list[tmp:]

for i in range(max(buyer_list) + 1):
    profit = 0
    price = i
    for j in range(len(buyer_list)):
        if price <= buyer_list[j]:
            profit += price

    if max_profit < profit:
        max_profit = profit
        max_price = i

print(max_price, max_profit)