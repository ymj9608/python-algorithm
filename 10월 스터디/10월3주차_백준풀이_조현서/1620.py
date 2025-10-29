# 나는야 포켓몬 마스터 이다솜
'''
딕셔너리 활용 => 이름과 번호 배정
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 이름 -> 번호
num_dict = {}
# 번호 -> 이름
name_dict = {}

for i in range(1, N + 1):
    pocketmon = input().strip()
    
    # 포켓몬이 나오면 해당 번호 배정
    num_dict[pocketmon] = i
    name_dict[i] = pocketmon

for _ in range(M):
    info = input().strip()

    # 정보가 포켓몬 이름이라면 번호 출력
    if info in num_dict.keys():
        print(num_dict[info])

    # 정보가 번호면 포켓몬 이름 출력
    else:
        print(name_dict[int(info)])