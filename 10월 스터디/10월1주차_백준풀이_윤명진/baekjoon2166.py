import sys
input = sys.stdin.readline

N = int(input())
locations = [list(map(int, input().split())) for _ in range(N)]


locations.append(locations[0])

sum1 = 0
sum2 = 0

# 신발끈 공식 적용 (Shoelace_formula.png 참조)
for i in range(N):
    sum1 += locations[i][0] * locations[i+1][1]
    sum2 += locations[i][1] * locations[i+1][0]

area = 0.5 * abs(sum1 - sum2)

print(round(area, 1))