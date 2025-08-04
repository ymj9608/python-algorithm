total=0
max_total=0
# 첫번쨰 역부터 10번째 역까지 반복
for i in range(10):
    get_out, get_in = map(int, input().split())
    
    # 각 역마다 탑승자 수 구하기
    total= total-get_out + get_in
    # 최대 탑승자 수 구하기
    if max_total < total:
        max_total = total
print(max_total)