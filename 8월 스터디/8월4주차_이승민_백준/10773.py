T=int(input())
list1=[]
for i in range(T):
    x=int(input())
    if x !=0:
        list1.append(x)
    else:
        list1.pop()
print(sum(list1))
