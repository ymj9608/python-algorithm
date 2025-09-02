my_str = input()

stack = []
real_str = ''
is_open = False  # 괄호 안인지 확인하는 변수

for char in my_str:
    # 1. '<' 문자를 만났을 때
    if char == '<':
        # 이전에 스택에 쌓인 단어가 있다면 결과에 뒤집어 추가
        while stack:
            real_str += stack.pop()
        is_open = True
        real_str += char  # '<'는 그대로 결과에 추가

    # 2. '>' 문자를 만났을 때
    elif char == '>':
        is_open = False
        real_str += char  # '>'는 그대로 결과에 추가

    # 3. 괄호 안에 있을 때
    elif is_open:
        real_str += char  # 태그 안의 문자는 그대로 결과에 추가

    # 4. 괄호 밖에 있을 때
    else:
        # 공백을 만났을 때
        if char == ' ':
            # 이전까지 스택에 쌓인 단어를 결과에 뒤집어 추가
            while stack:
                real_str += stack.pop()
            real_str += ' '  # 공백은 그대로 결과에 추가
        # 단어를 만났을 때
        else:
            stack.append(char) # 스택에 추가하여 뒤집을 준비

# 반복문이 끝난 후, 스택에 마지막 단어가 남아 있을 수 있으므로 처리
while stack:
    real_str += stack.pop()

print(real_str)