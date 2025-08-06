import sys

# input()은 한글자씩 입력할 때마다 임시저장소에 보관하지만
# sys.stdin.readline()은 입력을 한번에 받아서 최종값만 저장하므로 문자열의 크기가 크면
# sys.stdin.readline()이 압도적으로 빠름
# 다만, '', \n과 같은 개행 문자까지 모두 출력
# 또, input("숫자를 입력하세요: ")와 같이 프롬프트 메시지를 출력가능
# 카운팅 정렬 방식
N = int(sys.stdin.readline())

counts = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(1, 10001):
    if counts[i] > 0:
        for _ in range(counts[i]):
            print(i)

"""
메모리 초과한 코드 1
N = int(input())
my_list = []

for _ in range(N):
    my_list.append(int(input()))

my_list.sort()

for i in my_list:
    print(i)


메모리 초과한 코드 2
import sys

N = int(sys.stdin.readline())
my_list = []

for _ in range(N):
    my_list.append(int(sys.stdin.readline()))

my_list.sort()

for i in my_list:
    print(i)
"""