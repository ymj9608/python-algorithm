import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# X 좌표 계산
# (p + t)를 w로 나눈 몫과 나머지
delta_p = (p + t) // w
remainder_p = (p + t) % w

if delta_p % 2 == 0:  # 몫이 짝수 (정방향)
    final_p = remainder_p
else:  # 몫이 홀수 (역방향)
    final_p = w - remainder_p

# Y 좌표 계산
# (q + t)를 h로 나눈 몫과 나머지
delta_q = (q + t) // h
remainder_q = (q + t) % h

if delta_q % 2 == 0:  # 몫이 짝수 (정방향)
    final_q = remainder_q
else:  # 몫이 홀수 (역방향)
    final_q = h - remainder_q

print(final_p, final_q)