import sys

input = sys.stdin.readline

N, M = map(int, input().split())

my_dict_1 = dict()
my_dict_2 = dict()

for i in range(N):
    pocketmon = input().rstrip()
    # my_dict_1[포켓몬]: 등록 순서
    # my_dict_2[등록 순서]: 포켓몬
    # 으로 저장
    my_dict_1[pocketmon] = i+1
    my_dict_2[i+1] = pocketmon


for _ in range(M):
    check = input().rstrip()


    if check in my_dict_1.keys():
        print(my_dict_1[check])
    else:
        print(my_dict_2[int(check)])