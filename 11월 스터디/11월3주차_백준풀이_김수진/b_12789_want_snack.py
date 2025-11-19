from collections import deque

N = int(input())
students = list(map(int, input().split()))

stack = []
q = deque(students)

# 현재 간식 받을 수 있는 번호
can = 1

while q or stack:
    # 원래 줄에서 다 나왔는데 대기열 1번이 현재 번호와 다르면 종료
    if len(q) == 0 and stack[-1] != can:
        break
    # 원래 줄에 사람 있고, 첫 번째 사람이 현재 번호와 같으면 pop
    elif q and q[0] == can:
        q.popleft()
        can += 1
    # 대기열에 사람 있고, 첫 번째 사람(대기열 마지막 번호)이 현재 번호와 같으면 pop
    elif stack and stack[-1] == can:
        stack.pop()
        can += 1
    # 어디에도 없으면 원래 줄에서 대기열로 이동
    else:
        stack.append(q.popleft())

# 끝까지 받으면 can은 다음 숫자로 넘어가기 때문에 1 빼줌
if can-1 == N:
    print('Nice')
else:
    print('Sad')



# for i in range(N):
#     # 지금 학생이 간식 받을 수 있는 번호면
#     if students[i] == can:
#         # 받았다 치고 번호 +1
#         can += 1
#     # 만약 stack에 숫자가 있고, stack의 마지막과 can의 번호가 같으면 해당 번호 빼기
#     elif len(stack) >= 1 and stack[-1] == can:
#         can += 1
#         stack.pop()
#     else:
#         stack.append(students[i])
#     print(i, can)
#     print(stack)


        # # 만약 stack에 숫자가 있고, stack의 마지막과 can의 번호가 같으면 해당 번호 빼기
        # if len(stack) >= 1 and stack[-1] == can:
        #     check = True
        #     # 같은 번호라면 계속 뺄 예정
        #     while check == True and stack:
        #         stack.pop()
        #         can += 1
        #         # 번호가 달라지면 끝날 수 있도록
        #         if stack[-1] != can:
        #             check = False