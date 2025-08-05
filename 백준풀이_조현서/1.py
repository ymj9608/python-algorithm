# 테스트 케이스의 개수 T
T = int(input())

# 테스트 케이스를 1부터 출력하기에 1부터 시작
for test_case in range(1, T+1):
    # 수열의 길이 N
    N = int(input())
    # 수열의 원소들
    sequence = list(map(int, input().split()))

    # 연속되는 1의 개수 중 최댓값
    max_count = 0
    # 현재 연속되는 1의 개수
    current_count = 0

    # 수열을 순회하면서 연속되는 1의 개수를 세기
    for number in sequence:
        if number == 1:
            current_count += 1
            # 현재 연속되는 1의 개수가 최댓값보다 크면 갱신
            if current_count > max_count:
                max_count = current_count
        
        # number == 1이 아니면 연속되는 개수를 다시 처음부터 세야하므로
        else:
            current_count = 0


    print(f"#{test_case} {max_count}")