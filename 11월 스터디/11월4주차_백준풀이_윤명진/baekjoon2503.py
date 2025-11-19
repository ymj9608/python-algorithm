import sys

input = sys.stdin.readline

N = int(input())

numbers = set()

# 1~9 중복되지 않게 세 자리수 만들기
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and i != k and j != k:
                three_num = i * 100 + j * 10 + k
                # 각 자리를 비교하기 위해 문자열로 추가
                numbers.add(str(three_num))

for _ in range(N):
    thinking_number, strike, ball = map(int, input().split())
    thinking_number = str(thinking_number)
    result = set()
    for number in numbers:
        check_strike = 0
        check_ball = 0
        for i in range(3):
            # 수의 자리와 수가 일치하는 경우 strike
            if number[i] == thinking_number[i]:
                check_strike += 1

            # 수의 자리는 일치하지 않지만 number에 들어가 있는 경우 ball
            elif number[i] != thinking_number[i] and thinking_number[i] in number:
                check_ball += 1

        if check_strike == strike and check_ball == ball:
            result.add(number)

    # result는 이번 조건을 만족한 수들이므로 기존의 numbers와 교집합하여
    # 현재까지 모든 조건을 만족한 수들만 numbers에 남게 됨
    numbers = numbers.intersection(result)

print(len(numbers))