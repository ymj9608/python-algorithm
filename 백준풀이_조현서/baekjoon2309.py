
def solve():
    # 아홉 명의 난쟁이 리스트를 설정
    small_list1 = [int(input()) for _ in range(9)] 

    total = sum(small_list1)

    # 첫 번째 가짜 난쟁이를 도출하기 위한 반복문
    for i in range(9):
        # 두 번째 가짜 난쟁이를 도출하기 위한 반복문
        for j in range(i+1, 9):
            if total - (small_list1[i] + small_list1[j]) == 100:

                # 가짜 난쟁이 2명을 제외한 난쟁이들을 리스트에 담음
                result = [l for l in small_list1 if l != small_list1[i] and l != small_list1[j]]
                
                # 리스트를 오름차순으로 정렬 후 출력
                for r in sorted(result): 
                    print(r)
                return
solve()