# 카드2
'''
맨 처음 쌓인 카드를 버리고 그 다음의 카드를 맨 뒤로 넣음
# -> 그걸 반복하여 마지막 남은 카드를 구함.
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
'''
cards = []라고 썼다가 런타임 에러가 발생
'''
cards = deque()

# 카드 리스트에 N장만큼 담음
for i in range(1, N+1):
    cards.append(i)

# 한 장이 남을 때까지
# 맨 처음 카드를 빼고
# 다음 카드를 맨 뒤로 넣는 걸 반복
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

# 한 장이 남게 되면 출력
print(cards[0])
