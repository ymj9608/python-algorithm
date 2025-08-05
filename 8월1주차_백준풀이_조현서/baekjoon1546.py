# 시험 본 과목의 개수 N이 주어짐
N = int(input())

# 모든 점수를 리스트에 담음
scores = list(map(int, input().split()))
M = max(scores) # 최고 점수 M 설정

# 최고 점수를 기준으로 점수 조정한 후 리스트에 담음
control_scores = [(score/M)*100 for score in scores]

# 평균 점수 계산(모든 점수의 합/시험 본 과목의 개수 N)
average_score = sum(control_scores) / N

# 평균 점수 출력
print(average_score)    