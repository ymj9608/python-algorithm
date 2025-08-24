# 요세푸스 문제 0
'''
N명의 사람들이 원을 따라 앉아있고 K번째 사람을 제거하고
다음 K번째 사람을 제거하고를 반복하여 제거되는 순서를
구하는 것
-> 마지막 순서가 오면 다시 처음으로 가니까 원형 큐 문제같음
'''
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 사람들을 담을 큐 리스트 생성
people = deque()
# 제거된 사람들 순서를 담을 리스트
result = []

# 사람들을 큐 리스트에 담음
for i in range(1, N+1):
    people.append(i)

# 사람들이 모두 제거될 때까지 반복
while people:
    '''
    rotate 함수를 사용하여 K번째 사람을 제거
    ex. rotate(2)이면 뒤에서 앞으로 2개를 가져옴
    -> [1, 2, 3, 4, 5] -> [5, 4, 1, 2, 3]
    음수면 앞에서 뒤로 넘김.
    '''
    people.rotate(-K + 1)
    result.append(people.popleft()) 

print('<' + ', '.join(map(str, result)) + '>')
