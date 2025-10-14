# IOIOI
'''
IOI 패턴 찾기
I + OI로 계속 증가하는 형태
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

ans = 0
# IOI 개수를 셀 변수 cnt
cnt = 0
i = 0

# 3개씩 탐색(IOI 찾기)
while i + 2 < M:
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        # IOI 개수 증가 + 1
        cnt += 1
        # N번 연속되는 IOI를 찾으면 정답 + 1
        if cnt == N:
            ans += 1
            # 겹쳐있는 IOI 패턴이 있을 수도 있으므로
            # 카운트 -1한 상태로 계속 탐색
            cnt -= 1  

        # IOI의 마지막 I에서 다시 이어감
        i += 2 

    # IOI 못 찾으면 개수 초기화      
    else:
        cnt = 0
        # 한 칸씩 이동하면서 검사
        i += 1

print(ans)