import sys

input = sys.stdin.readline

N = int(input())

my_dict = dict()

for _ in range(N):
    number = int(input())
    # 아직 my_dict에 없다면 my_dict[number] = 1로 세팅
    if number not in my_dict:
        my_dict[number] = 1
    # 있다면, 1 더하기
    else:
        my_dict[number] += 1

max_number = max(my_dict.values())
min_num = float('inf')
for key, value in my_dict.items():
    # 최대 보유한 카드가 여러 개일 경우 배열에 저장하여 sort하지 않고
    # 가장 작은 값으로 min_num을 갱신하면 메모리 최적화 가능
    if value == max_number:
        min_num = min(min_num, key)

print(min_num)