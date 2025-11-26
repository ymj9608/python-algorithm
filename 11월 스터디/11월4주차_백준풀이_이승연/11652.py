import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

cnt = {}
for i in arr:
    # i가 있으면 i 반환 + 1
    # i가 없으면 0 반환 + 1
    cnt[i] = cnt.get(i, 0) + 1

# 정렬 순서 : 1. 가장 많이 갖고있는 정수 -> 2. 작은 정수부터
result = sorted(cnt.items(), key=(lambda x:(x[1],-x[0])), reverse=True)
print(result[0][0])