# 좌표 정렬하기
# 점의 개수 N이 주어짐
N = int(input())

list1 = []
# 각 점의 좌표를 입력받음
for _ in range(N):
    x, y = map(int, input().split())
    list1.append((x, y))

# 좌표를 x좌표 기준으로 정렬하고, x좌표가 같으면 y좌표 기준으로 정렬
list1.sort()    

for x, y in list1:
    print(x, y) # 정렬된 좌표 출력