import sys
input = sys.stdin.readline

N = int(input())
expression = input().rstrip()

alpha = [0] * N
for i in range(N):
    # A 부터 n번째 알파벳까지 번호 부여
    alpha[i] = int(input())

stack = []
for x in expression:
    # 알파벳이라면 수로 변환하여 stack에 push
    if 'A' <= x <= 'Z':
        value = alpha[ord(x) - ord('A')]
        stack.append(value)
        
    # 알파벳이 아니라면 연산자이므로 계산하기
    else:
        a = stack.pop()
        b = stack.pop()
        if x == '*':
            result = b * a
            stack.append(result)

        elif x == '+':
            result = b + a
            stack.append(result)

        elif x == '/':
            result = b / a
            stack.append(result)

        elif x == '-':
            result = b - a
            stack.append(result)

print(f'{stack[0]:.2f}')