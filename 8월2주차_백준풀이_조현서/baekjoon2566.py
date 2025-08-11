# 최댓값과 그에 해당하는 행과 열을 출력하는 문제

arr = []                                    # 리스트를 9*9로 담을 리스트 설정

for _ in range(9):                          # 1 ~ 9 번쨰 줄까지 리스트가 반복 생성
    nums = list(map(int, input().split()))
    arr.append(nums)                        # 한 줄씩 총 9줄이 포함
    

max_num = arr[0][0]                         # 반복되는 동안 최댓값이 초기화가 되지 않게 for문 밖에서 설정    
                                            # 격자판의 최댓값을 리스트 첫 행, 첫 열로 설정

row = 1                                     # 행과 열을 1로 설정(출력할 때 젤 첫번째 원소가 1행 1열이기 때문) 
col = 1                                     # -> 최댓값이 첫 설정 그대로 나왔을 때를 생각한 안전장치

                                            # 앞의 for문과 현재의 for문은 엄연히 별도의 for문이므로 밖에다 설정                                    
for i in range(9):                          # 행을 먼저, 열이 그 다음
    for j in range(9):                                           
        if arr[i][j] > max_num:             # 최댓값 갱신
            max_num = arr[i][j]             # 최댓값의 행과 열 갱신
            row = i + 1
            col = j + 1
                                
print(max_num)
print(row, col)            





