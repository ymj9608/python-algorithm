# A -> B
'''
B -> A로 생각
1. 짝수면 // 2
2. 끝자리 수가 1이면 1을 빼줌
위 과정을 반복
'''
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# 기본값이 1
count = 1  
while B > A:
    # 끝자리 수가 1이면
    # 끝자리를 뺀 몫만 가져감
    if B % 10 == 1:
        B //= 10
        count += 1
    
    # 짝수면 2로 나눔
    elif B % 2 == 0:
        B //= 2
        count += 1

    # 답이 나올 가능성이 없으면 즉시 종료
    else:
        break

print(count if B == A else -1)

# 시간 초과
# from collections import deque
# import sys
# input = sys.stdin.readline

# A, B = map(int, input().split())

# q = deque([(B, 1)])

# # bfs
# while q:
#     # 숫자와 카운트 한번에 꺼냄
#     num, count = q.popleft()

#     # 숫자가 A와 같아지면 카운트 출력
#     if num == A:
#         print(count)
#         break

#     # 짝수면 2로 나눔
#     if num % 2 == 0:
#         next_num = num // 2
#         # if next_num >= A:
#         q.append((next_num, count + 1))

#     # 끝자리 수가 1이면 1 제거
#     elif num % 10 == 1:
#         next_num = num // 10
#         # if next_num >= A:
#         q.append((next_num, count + 1))
    
#     # 이외에는 -1 출력
#     else:
#         print(-1)
#         break