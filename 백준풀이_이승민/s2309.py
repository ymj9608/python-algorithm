# 9명 입력
full_list=[]
for i in range(9):
    a=int((input()))
    full_list.append(a)
# 빈 리스트
answer_list=[]
# 이중for문 탈출을 위한 flag 변수

found=False   

# full_list에서 하나 빼기
for i in full_list:
    non_full_list = [x for x in full_list if x != i]
    #하나 뺀 non_full에서 하나 더 빼기
    for j in non_full_list:
        non_full_list2=[x for x in non_full_list if x != j]
        # 두개뺀 리스트의 합이 100이면 멈추기
        if sum(non_full_list2) == 100:
            answer_list = non_full_list2
            found = True
            break
    # 플래그 통해 이중for문 나오기    
    if found:
        break
#리스트 정렬
answer_list.sort()
for b in answer_list:
    print(b)
