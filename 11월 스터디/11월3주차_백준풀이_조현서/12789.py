# 도키도키 간식드리미
'''
대기열 줄의 뒤에 있는 사람이 나가는 구조
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stack = []
passing_num = 1

for num in nums:
    # 현재 순서가 대기 순서와 맞으면 통과
    if num == passing_num:
        passing_num += 1
    # 아니면 옆 줄에 세움
    else:
        stack.append(num)  

    # 옆 줄에서 가장 앞 번호가 대기 순서와 같으면 통과
    while stack and stack[-1] == passing_num:
        stack.pop()
        passing_num += 1

# 현재 줄을 모두 확인했으면 stack이 남아있으면 옆 줄 확인
while stack and stack[-1] == passing_num:
        stack.pop()
        passing_num += 1

# 다 통과하면 N + 1
if passing_num == N + 1:
     print('Nice')
else:
    print('Sad')