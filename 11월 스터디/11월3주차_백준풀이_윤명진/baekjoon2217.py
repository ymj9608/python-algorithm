import sys
input = sys.stdin.readline

N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

max_weight = 0
for i in range(N):
    # 로프를 정렬한 다음, 로프를 순회하며 최소 중량 로프 * 로프의 개수와 현재까지 가장 큰 중량을 비교하여
    # 최댓값 갱신
    max_weight = max(max_weight, ropes[i] * (i + 1))

print(max_weight)