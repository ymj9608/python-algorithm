# 첫째 줄에 N이 주어짐
N = int(input())

# 반복 횟수 0으로 설정
count = 0

# N을 num 변수에 할당
num = N

while True:
    count += 1
    # num의 십의 자리와 십의 자리와 일의 자리 숫자를 분리하여 합의 일의 자리만 가져옴
    num = (num % 10)*10 + (num//10 + num % 10) % 10

    if num == N:
        break

print(count)  # 반복 횟수 출력