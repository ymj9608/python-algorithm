# 정렬 문제는 sys.stdin.readline()이 좀더 빠른 입력이라, 시간초과 문제를 해결할 때 사용
import sys
N = int(sys.stdin.readline())
my_list = []

# 입력 횟수 N만큼 반복하여 띄어쓰기를 기준으로 my_list에 한 쌍씩 튜플로 저장
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    my_list.append((x, y))

# sort() 함수는 튜플 (x, y)에서 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순으로 정렬됨
my_list.sort()

# my_list의 튜플을 순회하며 x, y좌표를 한줄씩 출력
for x, y in my_list:
    print(x, y)