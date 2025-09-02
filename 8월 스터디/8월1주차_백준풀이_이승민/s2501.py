# 두 수 입력
N, K = map(int, input().split())

# K 리턴하는 함수 생성 
def func(N,K):
    list1=[]
    # 약수 리스트 생성
    for i in range(1,N+1):
        if N % i == 0:
            list1.append(i)
    #약수의 갯수가 k보다 작을 때 0
    #아니면 k번째 출력
    if len(list1) < K:
        return 0
    else:
        return list1[K-1]
print(func(N,K))

