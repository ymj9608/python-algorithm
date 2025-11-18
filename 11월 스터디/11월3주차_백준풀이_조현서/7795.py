# 먹을 것인가 먹힐 것인가
'''
1. 기존 코드는 시간 초과(일일이 비교)
2. b의 크기가 a 크기보다 작으면 바로 break(가지치기)
3. 이전 값도 누적되서 추가하는 형식으로 시간 단축
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 오름차순 정렬
    A.sort()
    B.sort()

    count = 0
    j = 0
    for i in range(N):
        for k in range(j, M):
            if B[k] < A[i]:
                j += 1
            else:
                break

        count += j
        
    print(count)

# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     # 내림차순 정렬
#     A.sort(reverse=True)
#     B.sort(reverse=True)

#     count = 0
#     for i in range(len(A)):
#         for j in range(len(B)):
#             if A[i] > B[j]:
#                 count += 1

#             # 아니면 무시하고 넘어감
#             else:
#                 continue

#     print(count)