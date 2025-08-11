# 수 찾기
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for char1 in b:
    if char1 in a:
        print('1')

    else:
        print('0')

