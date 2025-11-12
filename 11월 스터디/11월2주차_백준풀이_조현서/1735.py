# 분수 합
import sys
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# 분자
num = a1 * b2 + a2 * b1  
# 분모 
den = b1 * b2             

# 약분하기
x = num
y = den
# 분모가 0이 아니면 계속 진행
'''
1. x=31, y=35 → 31%35=31 → x=35, y=31
2. x=35, y=31 → 35%31=4  → x=31, y=4
3. x=31, y=4  → 31%4=3   → x=4, y=3
4. x=4, y=3   → 4%3=1    → x=3, y=1
5. x=3, y=1   → 3%1=0    → x=1, y=0 → 끝
마지막 1이 최대공약수
'''
while y != 0:
    x, y = y, x % y

# 최대공약수
g = x   

# 최대공약수로 나눔
print(num//g, den//g)