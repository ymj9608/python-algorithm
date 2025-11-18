import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))

def candy(arr):
    result = 1
    # 가로 확인
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            # 양옆 인접한 사탕이 같으면
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

    # 세로 확인
    for j in range(N):
        cnt = 1
        for i in range(N-1):
            # 위아래 인접한 사탕 같으면
            if arr[i][j] == arr[i+1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1
    return result

# 초기 상태의 먹을수있는사탕 개수
result = candy(arr)

# 가로로 교환
for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]:

            # 비교해서 교환할말 결정하기때문에 꼭 복사해서 교환해야함
            new_arr = [a[:] for a in arr]
            new_arr[i][j], new_arr[i][j+1] = arr[i][j+1], arr[i][j]

            # 최대 길이 계산 후 비교
            result = max(result, candy(new_arr))

# 세로로 교환
for j in range(N):
    for i in range(N-1):
        if arr[i][j] != arr[i+1][j]:

            # 비교해서 교환할말 결정하기때문에 꼭 복사해서 교환해야함
            new_arr = [a[:] for a in arr]
            new_arr[i+1][j], new_arr[i][j] = arr[i][j], arr[i+1][j]

            # 최대 길이 계산 후 비교
            result = max(result, candy(new_arr))

print(result)