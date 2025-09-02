#숫자 입력
T=int(input())

#점수 리스트 받기
origin_score= list(map(int,input().split()))
max_score=0

# 최고점 찾기
for i in origin_score:
    if max_score < i:
        max_score = i
# 새로운 평균 구하기 
print(sum(origin_score)*100/max_score/3)
