N, K = map(int, input().split())

my_list = [i for i in range(1, N+1)]

idx = 0
count = 0
N_K_list = []

# 아이디어는 큐와 같음
while my_list != []:
    idx += 1
    count += 1
    if count == K and idx <= len(my_list):
        count = 0
        a = my_list.pop(idx-1)
        idx -= 1
        N_K_list.append(a)
    elif count == K and idx > len(my_list):
        idx = 0
        count = 0
        a = my_list.pop(idx)
        N_K_list.append(a)

    # 인덱스가 my_list의 길이보다 커지면 다시 앞으로 오도록 수정
    elif count != K and idx > len(my_list):
        idx = 1

print(f'<{", ".join(map(str, N_K_list))}>')