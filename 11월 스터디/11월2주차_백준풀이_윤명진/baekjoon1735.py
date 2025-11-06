"""
유클리드 호제법
A, B의 최대공약수 구하기
1. A와 B중 큰 수를 작은 수로 나누기
2-1. 나누어 떨어지면 작은 수가 최대 공약수

2-2. 나누어 떨어지지 않으면
작은 수를 새로운 큰 수로, 나머지를 새로운 작은 수로 지정한 다음,
나누어 떨어질 때(1번 과정)까지 반복

예를 들어
42와 18의 최대공약수 구하기
42를 18로 나누면 몫:2, 나머지:6
새로운 큰 수: 18, 새로운 작은 수: 6
18을 6으로 나누면 나누어 떨어지므로
6이 42와 18의 최대 공약수임.
"""
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

# 통분
denominator = B * D
# 통분했을 때의 분자
molecule = A * D + B * C

# 분모와 분자의 최대공약수 구하기

# 분모가 더 큰 경우
if denominator >= molecule:
    big_num = denominator
    small_num = molecule
    while True:
        # 큰 수를 작은 수로 나누어 보기
        remain = big_num % small_num
        # 나머지가 0이면 small_num이 최대공약수
        if remain == 0:
            denominator //= small_num
            molecule //= small_num
            print(molecule, denominator)
            break

        # 나머지가 0이 아니면 나누는 수를 큰 수로, 나머지를 작은 수로 하여 다시 나눗셈 진행
        else:
            big_num = small_num
            small_num = remain

# 분자가 더 큰 경우
else:
    big_num = molecule
    small_num = denominator
    while True:
        # 큰 수를 작은 수로 나누어 보기
        remain = big_num % small_num
        # 나머지가 0이면 small_num이 최대공약수
        if remain == 0:
            denominator //= small_num
            molecule //= small_num
            print(molecule, denominator)
            break

        # 나머지가 0이 아니면 나누는 수를 큰 수로, 나머지를 작은 수로 하여 다시 나눗셈 진행
        else:
            big_num = small_num
            small_num = remain