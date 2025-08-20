# 미로 탐색
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

# 상, 하, 좌, 우 방향 델타 검색
dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]

visited = [(0, 0)]  # 방문한 곳을 기록할 리스트 설정
i = 0               # 리스트에서 현재 확인할 위치를 알려주기 위한 인덱스 변수

# 인덱스 변수가 리스트 길이랑 같아지면 반복 종료
while i < len(visited):
    # 시작 좌표 설정
    x, y = visited[i] 
    i += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 조건을 만족하게 되면 원래의 좌표에서 거리를 + 1 기록
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1 

            # 그 다음 좌표를 방문한 곳 리스트에 추가
            visited.append((nx, ny))

# 인덱스 값까지만 이동하므로 -1씩 인덱스값 처리
print(arr[N-1][M-1])
