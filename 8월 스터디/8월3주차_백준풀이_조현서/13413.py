# 오셀로 재배치
# 첨에 문제를 제대로 안 읽어서 문자를 서로 앞뒤만 바꿀 수 있는지로 이해해서 오류를 범함
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    current = input().strip()
    target = input().strip()

    # B를 W로 바꿔야하는 것 - change_B 
    # W를 B로 바꿔야하는 것 - change_W
    change_B = change_W = 0

    # 앞과 뒤의 문자를 서로 바꾸는 방법
    for i in range(N):              # 글자 수만큼 반복문
        if current[i] != target[i]:
            if current[i] == 'B':
                change_B += 1
            else:                   # 현재 글자가 'W' 이면
                change_W += 1

    count = max(change_W, change_B) # change_B와 change_W의 개수가 같으면 서로 바꾸면 되고 
                                    # 서로 다르면 서로의 차이만큼 뒤집기를 써야하므로 무조건 큰 쪽을 선택
    print(count)

