from collections import Counter

N = int(input())

book_list = []

for _ in range(N):
    book = input()
    book_list.append(book)

best_seller = sorted(Counter(book_list).items(), key=lambda x: (-x[1], x[0]))

print(best_seller[0][0])