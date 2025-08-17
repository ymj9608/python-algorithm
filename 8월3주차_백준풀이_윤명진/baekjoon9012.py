T = int(input())

for _ in range(T):
    my_str = input()
    while True:
        # 괄호가 홀수개이면 짝이 안맞으므로 NO 출력
        if len(my_str) % 2 != 0:
            print('NO')
            break
        # 빈 문자열을 입력하면 YES 출력
        elif len(my_str) == 0:
            print('YES')
            break

        # (는 있는데 )는 없으면 NO 출력
        elif '(' in my_str and ')' not in my_str:
            print('NO')
            break
        # (는 없는데 )는 있으면 NO 출력
        elif '(' not in my_str and ')' in my_str:
            print('NO')
            break

        # 마지막이 (로 끝나면 NO 출력
        elif my_str[-1] == '(':
            print('NO')
            break


        # 마지막 (의 인덱스를 찾고 그 인덱스에 1을 더한 것이 )이면 () 두개를 삭제하여 my_str 재할당
        # 그게 아니면 NO 출력
        else:
            last_index = my_str.rfind('(')
            if my_str[last_index + 1] == ')':
                my_str = my_str[:last_index] + my_str[last_index + 2:]
                continue
            else:
                print('NO')
                break
