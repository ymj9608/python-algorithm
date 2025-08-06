N, M = map(int, input().split())
my_list = list(map(int, input().split()))
new_list = []

# 3장 합이 M을 넘지 않는 케이스들만 new_list에 추가
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if my_list[i] + my_list[j] + my_list[k] <= M:
                new_list.append(my_list[i] + my_list[j] + my_list[k])

# new_list에서 최댓값 출력
print(max(new_list))