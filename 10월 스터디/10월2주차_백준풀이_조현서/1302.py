# 베스트셀러
'''
딕셔너리 value 값으로 count 넣어주기
ex. {'top': 2, 'kimtop': 3, ...}
'''
import sys
input = sys.stdin.readline

N = int(input())
sales = {}

for _ in range(N):
    title = input().strip()
    # 이미 제목이 딕셔너리에 있으면 + 1
    if title in sales:
        sales[title] += 1

    # 없으면 1로 만들어줌
    else:
        sales[title] = 1

# 딕셔너리 value값을 꺼내 최댓값 갱신
max_cnt = 0
for count in sales.values():
    if count > max_cnt:
        max_cnt = count

# 갯수가 동일하면 사전순
# 책 리스트를 만들어 담고 정렬 후 가장 첫번째 값 출력
book_list = []
for title, count in sales.items():
    if count == max_cnt:
        book_list.append(title)

book_list.sort()
print(book_list[0])