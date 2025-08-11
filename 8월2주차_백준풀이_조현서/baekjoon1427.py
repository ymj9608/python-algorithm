# 소트인사이드

N = list(input().strip())  # int로 받아서 내면 정수가 되기 때문에 정수는 반복가능한 객체가 아님 
                           # -> 리스트로 못 뽑아냄
length = 0

for char in N:             # 문자를 하나씩 꺼내면서 문자의 수 구함
    length += 1
    
for i in range(length):             # 문자의 수만큼 순회하면서 글자 하나당 비교하면서 위치를 바꿈 
    for j in range(i+1, length):    # 인접한 숫자를 비교하면서 큰 숫자는 앞으로 보냄(내림차순)
        if N[i] < N[j]:
            N[i], N[j] = N[j], N[i]
                           
print(''.join(N))          # join 함수를 사용해서 문자열을 붙여서 뽑아냄

# print(N)
