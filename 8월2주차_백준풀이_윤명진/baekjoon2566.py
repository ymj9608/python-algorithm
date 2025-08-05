my_list = []

# 9x9 행렬 입력
for columns in range(9):
    rows = list(map(int, input().split()))
    my_list.append(rows)

# max값을 (1, 1)에 위치한 값으로 세팅
my_max = my_list[0][0]
# (x, y) 좌표 초기값을 (0, 0)으로 세팅해서 한번 fail 나옴 ㅜ
max_row = 1
max_column = 1

# row와 column을 순회하며 최댓값 갱신하기
# 인덱스는 각각 1씩 더해주어야 행렬의 좌표가 나옴
for i in range(9):
    for j in range(9):
        if my_max < my_list[i][j]:
            my_max = my_list[i][j]
            max_row = i+1
            max_column = j+1

# 출력
print(my_max)
print(max_row, max_column)