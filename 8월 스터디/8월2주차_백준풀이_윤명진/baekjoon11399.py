N = int(input())

my_list = list(map(int, input().split()))

length = len(my_list)

# 카운팅 정렬 방식으로 my_list를 정렬
COUNTS = [0] * (max(my_list) + 1)
TEMP = [0] * len(my_list)

for i in range(length):
    COUNTS[my_list[i]] += 1


for i in range(max(my_list)):
    COUNTS[i+1] += COUNTS[i]

for i in range(length - 1, -1, -1):
    COUNTS[my_list[i]] -= 1
    TEMP[COUNTS[my_list[i]]] = my_list[i]

# 정렬된 TEMP의 누적합으로 TEMP 갱신
for i in range(len(TEMP)-1):
    TEMP[i+1] += TEMP[i]

# TEMP의 합 출력
print(sum(TEMP))