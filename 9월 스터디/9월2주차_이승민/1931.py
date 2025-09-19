N=int(input())
list1=[]
for i in range(N):
    a,b=map(int,input().split())
    list1.append((a,b))

list1.sort(key=lambda x: (x[1],x[0]))
count=0
last_end_time = 0


for start, end in list1:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)