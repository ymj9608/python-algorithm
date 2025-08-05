# 첫째 줄에 숫자 N이 주어짐
N = int(input())

# 반복 횟수 0으로 설정
count = 0

# N을 num 변수에 할당
num = N

while True:
    # while 문이 반복될 경우 카운트 증가
    count += 1

    # num의 가장 오른쪽 숫자가 새로운 수의 십의 자리가 되므로 *10
    # num의 십의 자리와 일의 자리 숫자를 분리하여 더한 값의 일의 자리만 가져옴
    num = (num % 10)*10 + (num//10 + num % 10) % 10

    # 계산된 값이 주어진 N과 다시 같아질 경우 break
    if num == N:
        break

print(count)  # 반복 횟수 출력