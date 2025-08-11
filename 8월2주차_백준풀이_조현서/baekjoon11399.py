# ATM
N = int(input())                     # 사람 수 N            
P = list(map(int, input().split()))  # 인당 걸리는 시간

for i in range(N):
    for j in range(i+1, N):
        if P[i] > P[j]:
            P[i], P[j] = P[j], P[i]  # 앞에 사람이 빨라야 전부 걸리는 시간이 최솟값이 되므로 
                                     # 오름차순으로 만듦
current_time = 0
total_time = 0

for t in P:
    current_time += t            # 현재까지 걸린 시간
    total_time += current_time   # 누적해서 걸린 시간(누적합)

print(total_time)




