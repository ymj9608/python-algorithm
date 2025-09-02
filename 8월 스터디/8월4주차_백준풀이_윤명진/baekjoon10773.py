K = int(input())
my_list = []

# stack으로 해결
for _ in range(K):
    num = int(input())

    # 0을 안외쳤으면 my_list에 추가
    if num != 0:
        my_list.append(num)

    # 0을 외쳤으면 가장 마지막에 들어온 수 제거
    else:
        my_list.pop(-1)

print(sum(my_list))