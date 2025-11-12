import sys
input = sys.stdin.readline

N = int(input())

people = list(map(int, input().split()))

stack = []

current_order = 1
while people:
    # 가장 앞에 있는 사람이 현재 순서라면 pop
    if people[0] == current_order:
        current_order += 1
        people.pop(0)

    # 대기열에서 가장 앞에 있는 사람이 현재 순서라면 pop
    elif stack and stack[-1] == current_order:
        current_order += 1
        stack.pop()

    # 가장 앞에 있는 사람과 대기열에 가장 앞에 있는 사람이 현재 순서가 아니면
    # 대기열로 이동
    else:
        stack.append(people.pop(0))

# 줄 서 있는 곳에 사람이 남아있지 않다면
# 대기열에 있는 사람들 순서 확인
while stack:
    current_person = stack.pop()
    if current_person == current_order:
        current_order += 1
    else:
        break

# 대기열에 사람이 남아있다면, 불가능하므로 Sad 출력
if stack:
    print('Sad')
else:
    print('Nice')