# 1번 카드가 제일 위
# N번 카드가 제일 아래
# 첫번째 동작 제일 위에 있는 카드를 바닥에 버림
# 그 다음 제일 위에 있는 카드를 밑으로 옮긴다.
#ex) 1234 -> 234 -> 342 이게 한턴
# -> 342 -> 42 -> 24 


# T= int(input())

# def func(N):
#     if len(lsit1) ==1:
#         return(int(list1))
#     else:
#         list1.pop()
#         list1[0],list1[len(list1)-1] = 

#     func


from collections import deque


# 입력을 빠르게 받기 위함
N= int(input())
# 1투버 N까지의 숫자로 deque를 초기화
cards= deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()
    # 2. 그 다음 , 제일 위에있는 카드를 제일 아래로 옮깁니다.
    # cards.append(car)
    cards.append(cards.popleft())
print(cards[0])