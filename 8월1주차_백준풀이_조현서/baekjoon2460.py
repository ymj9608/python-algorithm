# 최대 승객 수와 현재 승객 수 변수 초기값으로 설정
max_passengers = 0
current_passengers = 0

# 총 10개의 역을 가므로 10으로 설정하면 총 10번 반복
for i in range(0, 10):
    out_nums, in_nums = map(int, input().split()) # 추가되는 승객과 나가는 승객을 설정
    current_passengers += in_nums
    current_passengers -= out_nums
    
    max_passengers = max(max_passengers, current_passengers)

print(max_passengers)