import sys
input = sys.stdin.readline

N = int(input())

stars = ['*']

cnt = 1
while cnt < N:
    # 모든 행 왼쪽에 '* ' 오른쪽에 ' *'이 붙음
    for i in range(len(stars)):
        stars[i] = '* ' + stars[i] + ' *'

    # 첫번째 행과 가장 마지막 행에 '*'이 (4cnt + 1)개 붙는다.
    first_top = '*' * (4 * cnt + 1)

    # 두번째 행과 아래에서 두번째 행에
    # 처음과 마지막이 '*'이고 공백이 (4cnt - 1)개 붙는다.
    second_top = '*' + ' ' * (4 * cnt - 1) + '*'
    stars.insert(0, first_top)
    stars.insert(1, second_top)
    stars.append(second_top)
    stars.append(first_top)
    cnt += 1

for star in stars:
    print(star)