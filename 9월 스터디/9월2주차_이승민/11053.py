A=int(input())
list1= list(map(int, input().split()))

max_value=0
max_count=0
for i in range(A):
    count=0
    max_value=list1[i]
    for j in range(i+1,A):
        if max_value < list1[j]:
            max_value=list1[j]
            count+=1

    if max_count <count:
        max_count = count

print(max_count+1)