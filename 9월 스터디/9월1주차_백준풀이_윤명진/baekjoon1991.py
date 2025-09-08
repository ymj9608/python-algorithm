import sys
input = sys.stdin.readline

# 전위순회
def pre_order(T):
    if T == 0:
        return

    node = alphabet_to_number(T)
    if node:
        pre_list.append(T)
        pre_order(left[node])
        pre_order(right[node])

# 중위순회
def in_order(T):
    if T == 0:
        return

    node = alphabet_to_number(T)
    if node:
        in_order(left[node])
        in_list.append(T)
        in_order(right[node])

# 후위순회        
def post_order(T):
    if T == 0:
        return

    node = alphabet_to_number(T)
    if node:
        post_order(left[node])
        post_order(right[node])
        post_list.append(T)

# 노드가 알파벳이라 A~Z를 숫자에 대응시키는 함수
def alphabet_to_number(cha):
    my_dict = {
        '.': 0,
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }
    return my_dict[cha]

N = int(input())
my_list = [list(input().split()) for _ in range(N)]

left = [0] * 27
right = [0] * 27
par = [0] * 27

# 부모, 왼쪽 자식, 오른쪽 자식을 각각 리스트에 저장
for i in range(N):
    p, l, r = my_list[i][0], my_list[i][1], my_list[i][2]
    par[i] = my_list[i][0]

    if l != '.':
        left[alphabet_to_number(my_list[i][0])] = my_list[i][1]

    if r != '.':
        right[alphabet_to_number(my_list[i][0])] = my_list[i][2]

par.insert(0, 0)

pre_list = []
in_list = []
post_list = []

pre_order('A')
in_order('A')
post_order('A')
print(''.join(pre_list))
print(''.join(in_list))
print(''.join(post_list))