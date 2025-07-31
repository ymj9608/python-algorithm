# 백준 2460번 지능형 기차2

# 각 역에 사람 수 저장할 리스트 생성
# 0을 저장한 이유는 for문 돌릴 때 people_num이 빈리스트면 0번째 인덱스 값이 존재하지 않아서 오류나므로
# 0을 넣고 for문 돌린 후에 0을 삭제하면 됨
people_num = [0]


for i in range(10):
    minus_people, plus_people = map(int, input().split()) # 10번 승강장까지 내린 사람 수와 탄 사람수를 입력
    sum_people = people_num[i] - minus_people + plus_people # 현재역 사람 수 = 전역 사람 수 - 내린 사람 수 + 탄 사람 수
    people_num.append(sum_people) # 현재역 사람수를 people_num에 추가


# 초기에 people_num = [0]으로 세팅해놓았기 때문에
# people_num은 총 11개 요소를 가지고 있으므로 0번째 인덱스 삭제하여 1~10번역에 있는 사람의 수만
# 남기려면 0번째 인덱스를 삭제해야 함
del people_num[0]

# 1~10번 승강장 사람 수 중 최대 사람 수 출력
print(max(people_num))