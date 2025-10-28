# 체스판 다시 칠하기
'''
첫 번째에 나오는 문자를 기준으로 정하는 것
그 기준으로 첫 줄은 짝수 칸, 두 번째 줄은 홀수 칸 반복,,
'''
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(input().strip() for _ in range(N))

min_change = 1e9

# 왼쪽 위부터 시작
# 8 * 8 배열 탐색 
for start_row in range(N - 7):
    for start_col in range(M - 7):
        # 첫 칸이 B인 경우
        change_B = 0
        change_W = 0

        for i in range(8):
            for j in range(8):
                # 현재 색
                current_color = arr[start_row + i][start_col + j]

                # 첫 줄은 짝수 칸
                # 두 번째 줄은 홀수 칸
                # => 즉 지그재그 형태로 문자가 같아야 함
                if (i + j) % 2 == 0:
                    if current_color != 'B':
                        change_B += 1
                    if current_color != 'W':
                        change_W += 1

                # 홀수 칸은 반대로 진행        
                else:  
                    if current_color != 'W':
                        change_B += 1
                    if current_color != 'B':
                        change_W += 1

        min_change = min(min_change, change_B, change_W)

print(min_change)