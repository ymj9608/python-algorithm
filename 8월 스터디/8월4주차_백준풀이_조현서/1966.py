# 프린터 큐
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 문서 개수, 궁금한 문서의 인덱스
    N, M = map(int, input().split())
    # 중요도 리스트
    importance = list(map(int, input().split()))

    queue = deque()

    for i in range(N):
        queue.append((i, importance[i]))
    
    # 출력 순서 카운트    
    printer = 0

    while queue:
        # 일단 맨 앞 문서 꺼냄
        current = queue.popleft()
        curr_impo = current[1]
        
        # 현재 문서보다 더 높은 중요도가 있는지 확인
        higher = False
        for j, other_impo in queue:
            if other_impo > curr_impo:
                higher = True
                break

        # 중요한 문서가 뒤에 있으면
        # 현재 문서를 뒤에 다시 넣음
        if higher:
            queue.append(current)
        
        # 아니면 인쇄
        else:
            printer += 1
            # 그러다 현재 문서가
            # 궁금한 문서의 인덱스와 같아지면
            # 현재 출력 순서를 출력
            if current[0] == M:
                print(printer)
                break
