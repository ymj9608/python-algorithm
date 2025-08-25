# solved.ac(카운팅 정렬)
import sys
input = sys.stdin.readline

n = int(input())

# 아무 의견이 없다면 난이도는 0
if n == 0:
    print(0)

# 제시된 점수가 있다면 카운팅 정렬에 모두 담음
# 점수를 준 사람의 수를 모두 구함   
else:
    count = [0] * 31
    for _ in range(n):
        score = int(input())
        count[score] += 1
    
    # 제외시켜야 되는 사람
    # 15%에다가 반올림
    not_include = int(n*0.15 + 0.5)

    # 왼쪽부터 제외시킴
    # 양쪽 모두 똑같이 빼줘야 함
    left = not_include
    for i in range(1, 31):
        # 빼줘야 하는 사람이 0이 되면 break 
        if left == 0:
            break
        # i 점수를 준 사람이 있는데
        # 제외시켜야 하는 사람보다 적으면 모두 빼주면 됨
        if count[i] > 0:
            if count[i] <= left:
                left = left - count[i]
                count[i] = 0
            # 제외시킬 사람보다 크면 
            # 제외시킬 사람만큼만 빼주면 됨
            else:
                count[i] = count[i] - left
                left = 0
    
    # 반대로 오른쪽은 큰 수부터 내려오면서
    # 똑같이 해주면 됨
    right = not_include
    for i in range(30, 0, -1):
        if right == 0:
            break
        if count[i] > 0:
            if count[i] <= right:
                right = right - count[i]
                count[i] = 0
            else:
                count[i] = count[i] - right
                right = 0

    total_sum = 0
    total_cnt = 0
    for i in range(1, 31):
        # i 점수를 준 사람이 있다면
        if count[i] > 0:
            # i 점수 * i 점수를 준 사람 수
            total_sum += i * count[i]
            # i 점수를 준 사람을 모두 더 함
            total_cnt += count[i]

    aver = total_sum/total_cnt
    print(int(aver + 0.5))


