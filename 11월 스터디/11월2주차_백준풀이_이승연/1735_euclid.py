import sys
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

x = a*d +b*c
y = b*d

# 무조건 x가 y보다 크게 설정
if x <= y:
    x, y = y, x

# 1. y가 x의 약수인 경우 -> 정수로 바꾸고 출력
if x % y == 0:
    print((a*d+b*c)//y, (b*d)//y)

while x % y != 0:
    # 유클리드 호제법
    x = x % y

    # 2. 나머지가 1이면 기약분수 -> 그대로 출력
    if x == 1:
        print(a*d+b*c, b*d)
        break
    
    # 무조건 x가 y보다 크게 설정
    if x <= y:
        x, y = y, x

    # 3. y가 최대공약수가 되는순간 기약분수로 바꾸고 break
    if x % y == 0:
        print((a*d+b*c)//y,(b*d)//y)
        break