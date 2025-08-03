# N과 K 입력
N, K = map(int, input().split())

# N의 약수를 저장할 리스트 생성
div_list = []

# N을 1부터 N까지의 수로 나누어보며 나누어떨어질 경우 약수 리스트에 추가
for i in range(1, N+1):
    if N % i == 0:
        div_list.append(i)

# 문제 조건: 약수의 개수가 K보다 작으면 0을 출력
if len(div_list) < K:
    print(0)

# 문제 조건: 약수 리스트에서 K번째로 큰 수 출력
else:
    print(div_list[K - 1])