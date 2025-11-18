# 사탕 게임
'''
가장 긴 연속부분(행 or 열)을 골라 사탕의 최대 개수
교환 방법 
1. 사탕 교환은 오른쪽 사탕과 교환
2. 혹은 아래 사탕과 교환 가능
교환 후 탐색하면서 최대 길이 구간과 최댓값 구하기
'''
import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

max_eat = 1
for i in range(N):
    for j in range(N):

        # 1. 오른쪽에 있는 사탕과 교환
        if j + 1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # 한 행과 열에서의 
            # 같은 사탕의 최대 개수
            max_count = 1

            # 행 검사
            for r in range(N):
                count = 1
                for c in range(1, N):
                    if board[r][c] == board[r][c-1]:
                        count += 1
                    else:
                        if count > max_count:
                            max_count = count
                        # 최댓값 갱신 후 카운트 초기화
                        count = 1

                if count > max_count:
                    max_count = count

            # 열 검사
            for c in range(N):
                count = 1
                for r in range(1, N):
                    if board[r][c] == board[r-1][c]:
                        count += 1
                    else:
                        if count > max_count:
                            max_count = count
                        # 최댓값 갱신 후 카운트 초기화
                        count = 1

                if count > max_count:
                    max_count = count

            if max_count > max_eat:
                max_eat = max_count

            # 다시 원상복구
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 2. 아래쪽에 있는 사탕과 교환
        if i + 1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

            max_count = 1
            # 행 검사
            for r in range(N):
                count = 1
                for c in range(1, N):
                    if board[r][c] == board[r][c-1]:
                        count += 1
                    # 같은 사탕이 아니면
                    else:
                        if count > max_count:
                            max_count = count
                        # 최댓값 갱신 후 카운트 초기화
                        count = 1

                if count > max_count:
                    max_count = count

            # 열 검사
            for c in range(N):
                count = 1
                for r in range(1, N):
                    if board[r][c] == board[r-1][c]:
                        count += 1
                    else:
                        if count > max_count:
                            max_count = count
                        # 최댓값 갱신 후 카운트 초기화
                        count = 1

                if count > max_count:
                    max_count = count

            if max_count > max_eat:
                max_eat = max_count
            
            # 다시 원상복구
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_eat)