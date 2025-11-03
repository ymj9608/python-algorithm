import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 기둥의 왼쪽 위치 기준으로 오름차순 정렬
new_arr = sorted(arr, key=lambda x: x[0])

# 현재까지 가장 높은 기둥
max_h = 0
# max_h의 인덱스
max_idx = 0
for i in range(N):
    if new_arr[i][1] > max_h:
        # 높이와 인덱스 갱신
        max_h = new_arr[i][1]
        max_idx = i

result = 0
# 1) 왼쪽 영역
# 현재 계산중인 기둥의 왼쪽 위 꼭짓점이 (current_w, current_h)일 때
current_h = new_arr[0][1]
current_w = new_arr[0][0]

for i in range(1, max_idx + 1):
    if new_arr[i][1] >= current_h:
        result += (new_arr[i][0] - current_w) * current_h
        current_h = new_arr[i][1]
        current_w = new_arr[i][0]

# 2) 오른쪽 영역 (역순으로 순회)
current_h = new_arr[-1][1]
current_w = new_arr[-1][0]

# 리스트의 끝(N-2)부터 가장 높은 기둥의 바로 오른쪽(max_idx-1)까지
for i in range(N-2, max_idx-1, -1):
    if new_arr[i][1] >= current_h:
        result += (current_w - new_arr[i][0]) * current_h
        current_h = new_arr[i][1]
        current_w = new_arr[i][0]

# 기둥의 폭이 1이니까 
result += max_h  
print(result)