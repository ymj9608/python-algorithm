list1=[]
N= int(input())

# N회 입력 받아서 빈 리스트에 추가
for i in range(N):
    a,b = map(int, input().split())
    list1.append([a,b])
# 리스트 정렬하기
new_list= sorted(list1)

# 정렬된 리스트 언패킹 후  한줄씩 출력하기
for a,b in new_list:
    print(a,b)
