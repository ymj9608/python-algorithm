N,M=map(int,input().split())
list1=list(map(int, input().split()))
max_value=max(list1)
a=0
for i in range(max_value,-1, -1):
    count=0
    for j in range(N):
        if list1[j] > i:
            count += (list1[j] - i)
    if count >= M:
        a=i
        break
print(a)