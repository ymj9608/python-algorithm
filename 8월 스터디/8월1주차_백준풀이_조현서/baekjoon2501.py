# N과 K과 빈칸을 사이에 두고 주어짐
N, K = map(int, input().split())    

# 약수를 담을 리스트 설정
div_list = []     

# N까지 포함되야 하므로 범위를 N+1로 설정
for i in range(1, N+1):
    if N % i == 0:          # N % i == 0이면 i는 N의 약수
        div_list.append(i)  # 만약 i가 N의 약수라면 약수 리스트에 포함

if len(div_list) >= K:  # 약수의 개수가 K보다 크면 K번째로 작은 수를 출력 : K-1을 쓰는 이유는 인덱스는 0부터 세기 때문
    print(div_list[K-1])

else:
    print(0)    # 그 외에는 0으로 출력