# 정수 삼각형
'''
dp로 모든 경우의 수 고려
'''
import sys
input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

# dp 삼각형 형태만큼 생성
dp = [[0]*N for _ in range(N)]

# 꼭대기 값 = 자기 자신
dp[0][0] = tri[0][0]   

# 위에서 아래로
# 0은 자기 자신이므로 1부터 시작
for i in range(1, N): 
    # 한 층마다 인덱스 + 1개만큼 있음         
    for j in range(i+1):      
        # 맨 왼쪽 
        if j == 0:  
            dp[i][j] = dp[i-1][j] + tri[i][j]

        # 맨 오른쪽
        elif j == i:  
            dp[i][j] = dp[i-1][j-1] + tri[i][j]

        # 가운데 -> 왼쪽과 오른쪽 값 중 큰 값과 자기 자신을 더한 값 
        else:  
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[N-1]))   