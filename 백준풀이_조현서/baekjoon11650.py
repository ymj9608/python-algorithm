# 점의 개수 N이 주어짐
N = int(input())

# (x, y) 좌표를 받을 리스트 설정
list1 = []

# 점의 개수만큼 반복
for _ in range(N):
    # 각 점의 좌표를 입력받음
    x, y = map(int, input().split())
    # 좌표를 리스트에 담음
    list1.append((x, y))

# 좌표를 x좌표 기준으로 정렬하고, x좌표가 같으면 y좌표 기준으로 정렬
list1.sort()    

# 정렬된 좌표 출력
for x, y in list1:
    print(x, y) 