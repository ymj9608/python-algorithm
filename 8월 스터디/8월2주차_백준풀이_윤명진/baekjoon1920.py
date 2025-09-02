import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

# 이진 탐색으로 구현
for target in B:
    start = 0          # 탐색 범위의 시작 인덱스
    end = N - 1        # 탐색 범위의 끝 인덱스
    found = False      # 찾았는지 여부를 저장할 변수

    # start가 end보다 커지면 탐색할 범위가 없다는 뜻
    while start <= end:
        mid = (start + end) // 2  # 중앙 인덱스 계산

        # 목표값을 찾은 경우
        if A[mid] == target:
            found = True
            break
        # 목표값이 중앙값보다 큰 경우, 오른쪽 부분을 탐색
        elif A[mid] < target:
            start = mid + 1
        # 목표값이 중앙값보다 작은 경우, 왼쪽 부분을 탐색
        else:
            end = mid - 1

    # 찾았으면 1, 못 찾았으면 0 출력
    if found:
        print(1)
    else:
        print(0)