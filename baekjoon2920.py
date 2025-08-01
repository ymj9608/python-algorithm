# 8개의 음계 입력
my_list = list(map(int, input().split()))

# 12345678 순으로 입력하면 'ascending' 출력
if my_list == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
# 87654321 순으로 입력하면 'ascending' 출력
elif my_list == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
# 그 이외는 'mixed' 출력
else:
    print('mixed')