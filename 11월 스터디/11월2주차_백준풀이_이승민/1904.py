#n 정해져
#00의 갯수를 a개 1의 갯수를 b개
# 그러면 n을 2a + b 로 표현하는 법을 찾아
#그 뒤에 각 표현하는 법에 n개중 1의 갯수 b 선택하는 갯수 구하면 총 경우의수를 구할수 있겠지?
import math

N=int(input())
count=0
#a 구하기
A=N//2
for a in range(A+1):
    b= N - 2*a
    
    #전체 타일 수 
    c= a+b
    count += math.comb(c,b)
print(count)