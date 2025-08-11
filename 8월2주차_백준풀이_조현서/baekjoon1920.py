# 수 찾기(시간 초과)
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

length = 0 
for _ in range(N):
    length += 1

for i in range(length//2):
    left, right = i, length//2 -1
    






# 시간 초과
# for char1 in b:
#     if char1 in a:
#         print('1')

#     else:
#         print('0')