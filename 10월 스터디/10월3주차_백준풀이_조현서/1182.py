# 부분수열의 합
'''
백트래킹 개념으로 하나씩 다 해봄
'''
import sys
input = sys.stdin.readline

def dfs(idx, sum):
    global count
    # 전부 다 돌면
    if idx == N:
        # 합이 S가 되면 카운트 + 1
        if sum == S:
            count += 1
        return

    # 합을 더해주고 다음 인덱스
    dfs(idx + 1, sum + nums[idx])
    # 합을 더하지 않음
    dfs(idx + 1, sum)

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
dfs(0, 0)

# 공집합을 제외해야 함(이 부분때문에 답이 계속 틀림) 
if S == 0:
    count -= 1

print(count)