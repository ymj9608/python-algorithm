# 로프(아직 미통과)
import sys
input = sys.stdin.readline

N = int(input())
ropes = []

for _ in range(N):
    rope = int(input())
    ropes.append(rope)

ropes.sort()

max_weight = 0
for i in range(N):
    weight = ropes[i] * (N - i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)