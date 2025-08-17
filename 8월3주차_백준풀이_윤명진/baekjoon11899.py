my_str = input()

stack = []

for i in range(len(my_str)):
    # stack이 비어있으면 my_str[i] 추가
    if stack == []:
        stack.append(my_str[i])

    # my_str[i]가 (이면 stack에 ( 추가
    elif my_str[i] == '(':
        stack.append('(')

    # my_str[i]가 )이고 stack에 마지막으로 들어온 것이 (이 아니면 stack에 ) 추가
    elif my_str[i] == ')' and stack[-1] != '(':
        stack.append(')')

    # my_str[i]가 )이고 stack에 마지막으로 들어온 것이 (이면 stack에 마지막으로 들어온 ( pop
    elif my_str[i] == ')' and stack[-1] == '(':
        stack.pop()

# stack에 남아있는 괄호의 개수가 최종 정답
print(len(stack))