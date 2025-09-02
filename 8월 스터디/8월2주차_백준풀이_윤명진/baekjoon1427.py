# sys.stdin.readline()으로 입력 속도 최적화
# 이때 int로 입력하면 \n이 정수로 변환할 수 없으므로
# str 형태로 입력한 다음, .pop(-1)을 통해 리스트의 마지막 요소인 \n 제거
import sys
my_list = list(map(str, sys.stdin.readline()))
my_list.pop(-1)

# 역순으로 정렬
my_list.sort(reverse=True)

# 리스트의 각 숫자를 붙여서 한자리수로 출력
print("".join(map(str, my_list)))