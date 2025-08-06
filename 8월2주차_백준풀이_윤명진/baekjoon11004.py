# sys.stdin.readline()으로 입출력 속도 최적화
import sys
N, K = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))

# sort() 함수는 퀵정렬 알고리즘 기반으로 구현된 함수이므로
# 최악의 경우 nlogn 시간복잡도를 가지므로 제한 시간 이내에 통과 가능
my_list.sort()

# 앞에서부터 K번째 수 출력
print(my_list[K-1])