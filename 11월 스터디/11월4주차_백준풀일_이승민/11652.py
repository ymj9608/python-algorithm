# print(j)
import sys
input = sys.stdin.readline
N = int(input())
cards = {}
for _ in range(N):
    num = int(input())
    if num in cards:
        cards[num] +=1
    else:
        cards[num] = 1

# 결과 계산을 위한 변수
max_count=0
answer = 0

sorted_key = sorted(cards.keys())

for num in sorted_key:
    if cards[num] > max_count:
        max_count=cards[num]
        answer=num
print(answer)