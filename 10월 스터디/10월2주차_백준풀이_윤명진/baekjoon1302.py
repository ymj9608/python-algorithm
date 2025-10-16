import sys
input = sys.stdin.readline

N = int(input())
best_seller = dict()
for _ in range(N):
    book_name = input().rstrip()

    # best_seller에 책이 등록되지 않은 경우, 목록에 추가
    if book_name not in best_seller:
        best_seller[book_name] = 1

    # best_seller에 책이 등록된 경우, 카운트 1 더하기
    else:
        best_seller[book_name] += 1

# 최대 판매량
max_sell = max(best_seller.values())

best_list = []
for key, value in best_seller.items():
    # 최대 판매량을 가진 책이 여러개일 경우, 정렬을 위해 리스트에 담기
    if value == max_sell:
        best_list.append(key)

best_list.sort()
# 사전순으로 가장 앞에 있는 책 제목 출력
print(best_list[0])