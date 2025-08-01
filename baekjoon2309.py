# 아홉난쟁이들의 키 입력
key_list = []
for _ in range(9):
    key = int(input())
    key_list.append(key)

# 난쟁이들의 키 합이 100이 되면 for문을 break를 하기 위해 is_finish 변수 생성
is_finish = False


# 1, 2 ~ 1, 9, ..., 8, 9 난쟁이들을 key_list를 제거해보면서 체크하기 위해 이중 for문 생성
# 총 경우의 수는 9C7=36, 즉 36번만 돌리면 돼서 시간복잡도가 높지 않음
for i in range(8):
    # key의 합이 100이 되면 for문을 멈추기 위해 if/else문으로 구성
    if is_finish is True:
        break
    else:
        for j in range(i+1, 9): 
            # i, j번째 인덱스에 위치한 난쟁이의 키를 빼보고 합이 100이 안되면 다시 추가하기 위해 key_1, key_2 변수에 저장
            key_1 = key_list[i] 
            key_2 = key_list[j]
            # 두 난쟁이의 키를 빼보기
            key_list.remove(key_1) 
            key_list.remove(key_2)
            # 키의 합이 100이 되면 for문을 종료하기 위해 is_finish의 값을 True로 변경하고 key_list 정렬하기, key_list의 있는 키들을 한줄씩 출력
            if sum(key_list) == 100:
                is_finish = True
                key_list.sort()
                for key in key_list:
                    print(key)
                break
            # 키의 합이 100이 되지 않으면 다시 key_1, key_2를 원래 인덱스 위치에 추가
            else:
                key_list.insert(i, key_1)
                key_list.insert(j, key_2)