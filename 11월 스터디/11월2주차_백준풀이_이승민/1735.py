a,b=map(int,input().split())
c,d=map(int,input().split())

num1= a*d+b*c
num11=a*d+b*c
num2 = b*d
num22=b*d

if num1> num2:
    while num1 % num2 !=0:
        num3=num1 % num2
        num1=num2
        num2=num3
    print(int(num11/num2), int(num22/num2))

if num2 > num1:
    while num2 % num1 !=0:
        num3 =num2 % num1
        num2=num1
        num1=num3
    print(int(num11/num1), int(num22/num1))