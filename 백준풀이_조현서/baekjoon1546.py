# 시험 본 과목의 개수 N이 주어짐
N = int(input())

scores = list(map(int, input().split()))
M = max(scores) # 최고 점수 M

# 최고 점수를 기준으로 점수 조정
control_scores = [(score/M)*100 for score in scores]
# 평균 점수 계산
average_score = sum(control_scores) / N

# 평균 점수 출력
print(average_score)    