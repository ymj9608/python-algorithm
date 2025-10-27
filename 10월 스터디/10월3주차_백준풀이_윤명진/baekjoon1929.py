min_num, max_num = map(int, input().split())

num_list = [False, False] + [True] * (max_num-1)

# 에라토스 테네스의 체
# True인 값은 소수, True인 값의 배수들은 모두 소수가 아니므로 False로 만듦.
# 예를 들어, 2는 True이므로 2를 제외한 2의 배수들 모두 False
# 3은 True이므로 3을 제외한 3의 배수들 모두 False
# 4는 2의 배수에서 False로 됐으므로 넘기고 5는 소수이므로 5의 배수들 모두 False...
for i in range(2, max_num+1):
    if num_list[i] is True:
        for j in range(i+i, max_num + 1, i):
            num_list[j] = False
# 주어진 범위 내에 소수들만 출력
for i in range(min_num, max_num+1):
    if num_list[i] is True:
        print(i)