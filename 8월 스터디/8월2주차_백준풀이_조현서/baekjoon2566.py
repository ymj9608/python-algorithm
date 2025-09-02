# 최댓값과 그에 해당하는 행과 열을 출력하는 문제
# 9 * 9 배열 생성
arr = [list(map(int, input().split())) for _ in range(9)]
max_num = arr[0][0]             # 격자판의 최댓값을 리스트 첫 행, 첫 열로 설정

row = 1                         # 행과 열을 1로 설정(출력할 때 젤 첫번째 원소가 1행 1열이기 때문)
col = 1                         # -> 최댓값이 첫 설정 그대로 나왔을 때를 생각한 안전장치

for i in range(9):              # 행을 먼저, 열이 그 다음
    for j in range(9):                                           
        if arr[i][j] > max_num: # 순회하면서 최댓값보다 크면 최댓값 갱신
            max_num = arr[i][j] # 최댓값의 행과 열 갱신(인덱스 값으로 순회하기 때문에 +1 해줌)
            row = i + 1
            col = j + 1
                                
print(max_num)
print(row, col)            





