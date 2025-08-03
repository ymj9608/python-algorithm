# 0보다 크거나 같고, 99보다 작거나 같은 정수 입력
N = int(input())

# N의 십의자리 수를 first_num, 일의 자리 수를 second_num에 저장
# N이 한자리 수여도 어차피 십의 자리 수는 0이 되기 때문에 굳이 if/else문으로 나누어 작성할 필요 X
first_num = N // 10
second_num = N % 10

# sum = N의 십의 자리 수 + N의 일의 자리 수
sum = first_num + second_num
# sum_1에 sum의 일의 자리 수 할당
sum_1 = sum % 10

# 연산 횟수를 저장할 변수 n 생성
n = 0
# 새로운 수와 N이 같아지면 반복문을 종료하기 위해 is_num이라는 변수를 False로 설정
is_num = False

# 새로운 수와 같아질 때까지 반복
while is_num is False:
    # new_num = N의 일의 자리 수 * 10  + sum_1
    # 예시) N = 26이면 sum = 2 + 6 = 8, sum_1은 8 % 10 = 8 => 새로운 수는 6 * 10 + 8 = 68
    new_num = second_num * 10 + sum_1 % 10

    # 새로운 수와 N이 같으면 반복문 종료하기 위해  is_num을 True로 바꾸고 n을 1만큼 더한 다음, 출력
    if new_num == N:
        n += 1
        is_num = True
        print(n)
    # 새로운 수와 N이 다르면 n을 1만큼 더하고 변수들을 위와 같은 과정으로 다시 설정한 다음, 반복하기
    else:
        n += 1
        first_num = new_num // 10
        second_num = new_num % 10
        sum = first_num + second_num
        sum_1 = sum % 10