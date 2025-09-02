# 단지 번호 붙이기
'''
모두 탐색하는 DFS 방식을 사용해야 할 듯
탐색된 집의 개수를 세서 단지별 리스트 만듦
'''
# import sys
# input = sys.stdin.readline
# 안 썼지만 채점하는데 오래 걸렸음

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)] 

# 방문 여부 확인하기 위한 배열
visited = [[0] * N for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

# 단지마다 집 개수를 담을 리스트
result = []

def dfs(x, y):
    # 현재 위치를 방문 처리
    visited[x][y] = 1
    # 현재 건물의 개수를 포함 +1
    count = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny)
    
    return count

# 지도 전부 다시 확인
for i in range(N):
    for j in range(N):
        # 아직 방문 안 한 집 발견하면
        if arr[i][j] == 1 and not visited[i][j]:
            # 연결된 집 개수 세기
            house = dfs(i, j)
            # 한 단지가 모두 끝나면 리스트에 추가
            result.append(house)

# 단지 개수를 출력
print(len(result))
# 각 단지를 오름차순으로 정렬하여 출력
for r in sorted(result):
    print(r)    
