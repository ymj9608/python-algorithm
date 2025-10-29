from itertools import permutations
import sys

input = sys.stdin.readline

def calculate_score(li):
    global max_score
    idx = 0
    total_score = 0

    for inning in range(N):
        # 이닝마다 루와 아웃카운트 초기화
        bases = [0, 0, 0]  # 1루, 2루, 3루
        out_count = 0

        while out_count < 3:
            hit = players[inning][li[idx]]

            if hit == 0:  # 아웃
                out_count += 1

            elif hit == 1:  # 안타
                total_score += bases[2]  # 3루 주자 득점
                bases[2] = bases[1]
                bases[1] = bases[0]
                bases[0] = 1

            elif hit == 2:  # 2루타
                total_score += bases[2] + bases[1]  # 3, 2루 주자 득점
                bases[2] = bases[0]
                bases[1] = 1
                bases[0] = 0

            elif hit == 3:  # 3루타
                total_score += sum(bases)  # 모든 주자 득점
                bases = [0, 0, 1]  # 타자는 3루로

            elif hit == 4:  # 홈런
                total_score += sum(bases) + 1  # 모든 주자 + 타자 득점
                bases = [0, 0, 0]  # 루 초기화

            # 다음 타자 설정
            idx = (idx + 1) % 9

    # N이닝 종료 후 최대 점수 갱신
    max_score = max(max_score, total_score)


N = int(input())

players = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

# 1~8번 선수 (인덱스 1~8)로 순열 생성
for p in permutations(range(1, 9), 8):
    ordered_lineup = list(p)
    # 4번 타자(인덱스 3)에 0번 선수 삽입
    ordered_lineup.insert(3, 0)

    calculate_score(ordered_lineup)

print(max_score)