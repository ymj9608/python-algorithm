N = int(input())

if N == 1:
    print(1)
else:
    # 카드의 수가 짝수이면 한 번 반복하고 난 다음, 2, 4, 6, 8, ...이 남음
    if N % 2 == 0:
        my_list = [2 * i for i in range(1, N // 2 + 1)]
    
    # 카드의 수가 홀수이면 한 번 반복하고 나면, 4, 6, 8, ..., N-1, 2가 남음
    else:
        my_list = [2 * i for i in range(2, N // 2 + 1)]
        my_list.append(2)
    
    # 짝수이면 남은 카드가 위와 같은 방법으로 짝수번째 카드들만 남도록 재귀함수로 구현
    # 홀수이면 남은 카드가 위와 같은 방법으로 맨위의 카드를 제외한, 4번째, 6번째, 8번째, ..., N-1번째, 첫번째 카드가 남게함.
    # 1장이 남으면 그 카드가 마지막에 남게되는 카드이므로 그 카드를 반환
    def even_num_list(lst):
        n = len(lst)
        if n % 2 == 0:
            new_list = [lst[2*i - 1] for i in range(1, n // 2 + 1)]
            return even_num_list(new_list)
        elif len(lst) == 1:
            return lst[0]
        else:
            new_list = [lst[2*i - 1] for i in range(1, n // 2 + 1)]
            new_list.insert(0, lst[-1])
            return even_num_list(new_list)

    result = even_num_list(my_list)
    print(result)