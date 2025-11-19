from collections import deque

N = int(input())
students = list(map(int, input().split()))

target = 1
stack = deque()
snack = []

for i in range(N):
    if students[i] == target:
        snack.append(students[i])
        target += 1
    else:
        stack.appendleft(students[i])

    while stack and stack[0] == target:
        check = stack.popleft()
        if check == target:
            snack.append(check)
            target += 1

if not stack:
    print('Nice')
else:
    print('Sad')