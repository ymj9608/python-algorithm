# 한수
'''
등차수열을 이루는 수
1. 한 자리 수는 한수
2. 두 자리 수도 하나의 등차만 이루니까 한수
3. 세 자리 수부터는 등차가 일정한지 확인해야 함
4. 1000은 한수가 아니므로 고려 X
'''
import sys
input = sys.stdin.readline

N = int(input())

count = 0
for i in range(1, N + 1):
    # 한, 두 자리 수는 무조건 등차수열
    if i < 100:
        count += 1
    
    # 세 자리 수부터는 각 자리 수를 구함
    else:
        # 백의 자리
        a = i // 100
        # 십의 자리
        b = (i // 10) % 10
        # 일의 자리
        c = i % 10

        # 각 자리 수가 일정한 등차를 가지고 있다면 카운트
        if (a - b) == (b - c):
            count += 1

print(count) 