# 알파벳
'''
ord 함수 사용
-> 아스키 코드 
'A' => 65, 'B' => 66...
'''
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]

# 알파벳 개수만큼 방문 배열 생성
used = [False] * 26

# 상하좌우 델타 
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 시작칸 포함해야하므로
ans = 1  

def dfs(y, x, cnt):
    global ans
    if cnt > ans:
        ans = cnt
        # 알파벳 개수만큼 되면 조기 종료
        if ans == 26:  
            return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위 내에서
        if 0 <= ny < R and 0 <= nx < C:
            next_ch = arr[ny][nx]
            # A의 아스키 코드는 65이므로 65부터 시작
            k = ord(next_ch) - 65

            # 사용하지 않았던 알파벳이면 사용 처리
            if not used[k]:
                used[k] = True
                dfs(ny, nx, cnt + 1)
                # 백트래킹
                used[k] = False  

# 시작칸부터 탐색 시작
start = ord(arr[0][0]) - 65
used[start] = True
dfs(0, 0, 1)

print(ans)