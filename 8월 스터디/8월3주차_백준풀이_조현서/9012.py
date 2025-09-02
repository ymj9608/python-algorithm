# 괄호
T = int(input())

for _ in range(T):
    s = input().strip()

    stack = []
    valid = True  # 오류값을 설정하기 위함

    for char in s:
        if char == '(':
            stack.append(char)  # 여는 괄호 추가
        else:
            if stack:           # ')'가 나오고 스택 안에 값이 있으면 pop
                stack.pop()
            else:               # 비어있는데 괄호가 닫는 괄호가 나오면 오류
                valid = False
                break

    if valid and not stack:    # 스택이 비어있고 오류가 없으면 YES
        print('YES')
    else:                      # 아니면 NO
        print('NO')