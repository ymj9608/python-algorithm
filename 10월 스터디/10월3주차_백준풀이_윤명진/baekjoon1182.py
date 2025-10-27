import sys
input = sys.stdin.readline

# 백트래킹
def find_number_of_subset(total_sum, idx):
    global count 
    if idx == N:
        if total_sum == S:
            count += 1
        return
    
    # idx번째 수를 더하기
    find_number_of_subset(total_sum, idx + 1)
    # idx번째 수를 더하지 않기
    find_number_of_subset(total_sum + subset[idx], idx + 1)


N, S = map(int, input().split())
subset = list(map(int, input().split()))
count = 0
find_number_of_subset(0, 0)

# S가 0이면 공집합도 count되므로 1 빼주기
if S == 0:
    count -= 1

print(count)
