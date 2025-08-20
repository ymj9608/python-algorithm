s = input().strip()     # 문자열 입력

stack = []              # 거꾸로 만들기 위한 스택 리스트 설정
in_tag = False          # 현재 괄호 내부인지를 확인하기 위함
result = ''             # 최종 결과를 담을 문자열

for char in s:          # 문자를 순회하면서
    if char == '<':     # < 문자가 있다면
        while stack:    # 이전에 스택에 있는 문자가 있었다면 거꾸로 만들어서 문자열에 추가
            result += stack.pop()
        in_tag = True   # 여는 괄호를 만났으므로 현재 괄호 내부
        result += char  # <는 결과에 그대로 추가 

    elif char == '>':
        in_tag = False  # 닫는 괄호를 만났으므로 현재 괄호 외부
        result += char  # 닫는 괄호 자체는 결과에 그대로 추가 

    elif in_tag:        # 괄호 내부에 있다면 문자 그대로 결과에 추가
        result += char

    else:               # 괄호 밖에 있다면
        if char == ' ': # 문자가 공백이라면 이전까지의 스택에 있던 것을 
                        # 거꾸로 만들어서 결과에 추가, 공백은 그대로 추가
            while stack:
                result += stack.pop()
            result += ' '
        
        else:           # 공백이 아닌 문자를 만나면 스택에 추가(거꾸로 만들어야 하므로)
            stack.append(char)

while stack:            # 스택에 문자가 있으면 거꾸로 만들어서 추가
    result += stack.pop()

print(result)
                     