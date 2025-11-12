import math

a, b = map(int, input().split())
c, d = map(int, input().split())

gcd = math.gcd(b, d)

x = ((a * d) + (b * c)) // gcd
y = (b * d) // gcd

r = math.gcd(x, y)
print(x // r, y // r)